import random

def select_random_row(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    result = select_random_row(sample_data)
    print(result)