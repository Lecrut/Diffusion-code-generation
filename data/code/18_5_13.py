def find_middle(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    mid_index = len(arr) // 2
    mid_value = arr[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [1, 2, 3, 4, 5, 6]
    ]
    for case in test_cases:
        index, value = find_middle(case)
        print(f"Array: {case} | Middle Index: {index} | Middle Value: {value}")