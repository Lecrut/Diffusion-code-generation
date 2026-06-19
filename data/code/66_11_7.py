def find_violating_pairs(arr):
    violations = []
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            violations.append(arr[i])
    return violations

if __name__ == '__main__':
    sample_array = [1, 3, 2, 5, 4, 7]
    result = find_violating_pairs(sample_array)
    print(result)