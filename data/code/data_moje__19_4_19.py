import random

def select_random_row(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return random.choice(data)

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        ['a', 'b', 'c'],
        [10.5, 20.7, 30.9],
        ['x', 'y', 'z']
    ]
    result = select_random_row(sample_data)
    print(result)