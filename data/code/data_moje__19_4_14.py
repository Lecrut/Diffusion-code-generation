import random

def select_random_row(data):
    if not data:
        raise ValueError("The input list cannot be empty.")
    return random.choice(data)

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    result = select_random_row(sample_data)
    print(result)