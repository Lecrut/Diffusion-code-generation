import numpy as np

COMPARISON_RESULTS = {
    'increasing': arr[i] < arr[i + 1],
    'decreasing': arr[i] > arr[i + 1],
    'equal': arr[i] == arr[i + 1]
}

def compare_consecutive_elements(arr):
    results = []
    for i in range(len(arr) - 1):
        for key, condition in COMPARISON_RESULTS.items():
            if condition:
                results.append(key)
                break
    return results

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 2, 1])
    result = compare_consecutive_elements(sample_array)
    print(result)