def main():
    matrix_1 = get_matrix()
    print(matrix_1)
    matrix_2 = get_matrix()
    print(matrix_2)
    print(add_matrix(matrix_1,matrix_2))

def get_matrix():
    #grab user input for rows & collumns, empty matrix to be returned.
    row = int(input("enter num rows: "))
    col = int(input("enter num columns: "))
    matrix = []
    #appends empty list for reach row
    for i in range(row):
        matrix.append([])
        #for each column in a row, prompts user input and appends to list at matrix[i]
        for j in range(col):
            matrix[i].append(input("Input Row " + str(i+1) + " Column " + str(j+1) + ": "))
    return matrix

def add_matrix(mat1, mat2):
    rmatrix = []
    #if the # of rows in mat1 & mat2 are equal, and columns in row 1 are equal
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        #appends empty list for each row
        for i in range(len(mat1)):
            rmatrix.append([])
            #for columns in row, appends  with mat1[(row)][(column)] + mat2[(row)][(column)]
            for j in range(len(mat1[0])):
                rmatrix[i].append(int(mat1[i][j]) + int(mat2[i][j]))
    #if matrices are unequal, prints error and returns error value (-1)
    else:
        print("The matrices are not compatible for addition/subtraction.")
        rmatrix = -1
    return rmatrix

if __name__ == '__main__':
    main()
