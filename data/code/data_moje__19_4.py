import random

def select_random_row(data):
    return random.choice(data)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = select_random_row(matrix)
    print(result)