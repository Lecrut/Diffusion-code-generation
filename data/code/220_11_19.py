import numpy as np

def calculate_average(numbers):
    return np.mean(numbers)

if __name__ == '__main__':
    sample_sets = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    averages = [calculate_average(set) for set in sample_sets]
    print(averages)