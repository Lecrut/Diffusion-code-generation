import numpy as np

def calculate_average_pairs(arr):
    pairs = [(arr[i], arr[i+1]) for i in range(len(arr)-1)]
    averages = [np.mean(pair) for pair in pairs]
    return np.array(averages)

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5])
    result = calculate_average_pairs(sample_array)
    print(result)