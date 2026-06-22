import numpy as np

def calculate_averages():
    sets = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    arrays = np.array(sets)
    averages = np.mean(arrays, axis=1)
    return averages

if __name__ == '__main__':
    result = calculate_averages()
    print(result)