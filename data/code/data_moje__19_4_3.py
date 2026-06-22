import random

def select_random_row(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return random.choice(data)

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
        [100, 110, 120],
        [130, 140, 150]
    ]
    selected = select_random_row(sample_data)
    print(selected)