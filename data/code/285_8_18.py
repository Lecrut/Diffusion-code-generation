import numpy as np

comparison_map = {
    1: 'increasing',
    -1: 'decreasing',
    0: 'equal'
}

def compare_consecutive_elements(arr):
    results = []
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        results.append(comparison_map.get(diff, 'unknown'))
    return results

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 2, 1])
    print(compare_consecutive_elements(sample_array))