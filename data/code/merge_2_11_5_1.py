def is_uniform_matrix(matrix):
    for row in matrix:
        if len(set(row)) > 1:
            return False
    return True
if __name__ == '__main__':
    sample_matrices = [
        [[1, 1], [2, 2]],
        [[1, 2], [3, 4]],
        [[5], [6]]
    ]
    for i, mat in enumerate(sample_matrices):
        result = is_uniform_matrix(mat)
        print(f"Matrix {i + 1} {'is' if result else 'is not'} uniform.")