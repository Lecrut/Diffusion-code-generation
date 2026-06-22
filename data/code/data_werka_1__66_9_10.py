def is_valid_array(arr):
    return isinstance(arr, list) and all(isinstance(x, int) for x in arr)

def find_adjacent_greater_pairs(arr):
    if not is_valid_array(arr):
        raise ValueError("Input must be a list of integers")
    
    indices = []
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_array = [3, 5, 2, 8, 6, 7, 4]
    result = find_adjacent_greater_pairs(sample_array)
    print(result)