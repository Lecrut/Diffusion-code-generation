def compare_adjacent_elements(arr):
    if len(arr) < 2:
        return []
    
    result = []
    for i in range(1, len(arr)):
        result.append(arr[i] > arr[i - 1])
    
    return result

if __name__ == '__main__':
    sample_array = [7, 3, 5, 2, 8, 6]
    result = compare_adjacent_elements(sample_array)
    print(result)