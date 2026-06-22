import numpy as np

def compare_consecutive_elements(arr):
    comparisons = {
        'increasing': lambda x, y: x < y,
        'decreasing': lambda x, y: x > y,
        'equal': lambda x, y: x == y
    }
    results = []
    for i in range(len(arr) - 1):
        if comparisons['increasing'](arr[i], arr[i + 1]):
            results.append('increasing')
        elif comparisons['decreasing'](arr[i], arr[i + 1]):
            results.append('decreasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 2, 1])
    print(compare_consecutive_elements(sample_array))