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
    sample_array = np.array([3, 5, 2, 8, 6, 7])
    print(compare_consecutive_elements(sample_array))