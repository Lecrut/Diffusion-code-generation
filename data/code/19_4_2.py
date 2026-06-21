import random

def select_random_row(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return random.choice(data)

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    selected = select_random_row(sample_data)
    print(selected)