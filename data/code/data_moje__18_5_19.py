def find_middle(arr):
    length = len(arr)
    middle_index = length // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [1, 2],
        [5, 10, 15, 20, 25, 30],
    ]

    for arr in test_cases:
        mid_idx, mid_val = find_middle(arr)
        print(f"Array: {arr}")
        print(f"Middle Index: {mid_idx}")
        print(f"Middle Value: {mid_val}")
        print()