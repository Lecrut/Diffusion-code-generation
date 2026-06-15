def print_square_matrix(matrix):
    n = len(matrix)
    if n == 0:
        return
    for row in matrix:
        print(" ".join(map(str, row)))
if __name__ == '__main__':
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_square_matrix(sample_matrix)