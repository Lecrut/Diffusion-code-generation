def find_adjacent_violations(arr):
    if not isinstance(arr, list) or not all(isinstance(x, float) for x in arr):
        raise ValueError("Input must be a list of floats.")
    
    violations = []
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            violations.append(i)
    return violations

if __name__ == '__main__':
    sample_array = [1.0, 3.0, 2.0, 5.0, 4.0, 6.0, 7.0]
    try:
        result = find_adjacent_violations(sample_array)
        print(result)
    except ValueError as e:
        print(e)