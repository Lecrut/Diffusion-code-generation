import numpy as np

def compare_consecutive_elements(arr):
    results = []
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            results.append('increasing')
        elif arr[i] > arr[i + 1]:
            results.append('decreasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_array = np.array([1, 3, 2, 4, 4, 5])
    print(compare_consecutive_elements(sample_array))