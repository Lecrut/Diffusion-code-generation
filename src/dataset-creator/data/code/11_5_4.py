import numpy as np
def check_uniform_matrix(matrix):
    return all(np.all(row[0] == row) for row in matrix)
if __name__ == '__main__':
    sample1 = [[1, 1], [2, 2]]
    sample2 = [[1, 2], [3, 4]]
    print(check_uniform_matrix(sample1))
    print(check_uniform_matrix(sample2))