import numpy as np
COMPARISON_MAP = {1: 'increasing', -1: 'decreasing', 0: 'equal'}

def compare_consecutive_elements(arr):
    results = []
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        result = COMPARISON_MAP[diff]
        results.append(result)
    return results
if __name__ == '__main__':
    sample_array = np.array([1, 2, 5, 4, 3, 8, 9, 10])
    print(compare_consecutive_elements(sample_array))