def find_violations(arr):
    THRESHOLD = 0.0
    violations = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i + 1] > arr[i] + THRESHOLD:
            violations.append((i, i + 1))
    return violations

if __name__ == '__main__':
    sample_array = [1.0, 2.0, 3.0, 5.0, 4.0, 6.0, 7.0]
    result = find_violations(sample_array)
    for start, end in result:
        print(f"Indices: ({start}, {end})")