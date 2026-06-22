def find_violating_pairs(arr):
    if not isinstance(arr, list) or not all(isinstance(x, float) for x in arr):
        raise ValueError("Input must be a list of floats.")
    
    violating_elements = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i+1] < arr[i]:
            violating_elements.append(arr[i])
    return violating_elements

if __name__ == '__main__':
    sample_array = [1.0, 3.0, 2.5, 5.0, 4.0, 6.0, 7.0]
    result = find_violating_pairs(sample_array)
    print(result)