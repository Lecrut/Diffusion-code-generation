import random

def select_random_row(matrix):
    if not matrix:
        raise ValueError("Matrix must not be empty")
    return random.choice(matrix)

if __name__ == '__main__':
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(select_random_row(sample_matrix))