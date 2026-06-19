def find_violating_pairs(arr):
    n = len(arr)
    violating_elements = []
    for i in range(n - 1):
        if arr[i + 1] < arr[i]:
            violating_elements.append(arr[i + 1])
    return violating_elements

if __name__ == '__main__':
    sample_array = [1.0, 3.5, 2.0, 5.0, 4.0, 6.0, 7.0]
    result = find_violating_pairs(sample_array)
    print(result)