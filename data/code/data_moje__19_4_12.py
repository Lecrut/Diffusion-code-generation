import random

def select_random_row(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return data[random.randrange(len(data))]

if __name__ == '__main__':
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(select_random_row(sample_matrix))
    print(select_random_row(sample_matrix))
    print(select_random_row(sample_matrix))