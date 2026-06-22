import random

def select_random_row(matrix):
    return random.choice(matrix)

if __name__ == '__main__':
    sample_matrix = [[1, 2], [3, 4], [5, 6]]
    result = select_random_row(sample_matrix)
    print(result)