def find_middle(array):
    n = len(array)
    if n == 0:
        return None, None
    middle_index = n // 2
    middle_value = array[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], (2, 3)),
        ([10, 20, 30, 40], (2, 30)),
        ([42], (0, 42)),
        ([1, 2], (1, 2)),
        ([5, 15, 25, 35, 45, 55], (3, 35)),
        ([], (None, None))
    ]
    
    for arr, expected in test_cases:
        idx, val = find_middle(arr)
        assert idx == expected[0] and val == expected[1], f"Failed for {arr}: got ({idx}, {val}), expected {expected}"
        print(f"Array: {arr} -> Middle Index: {idx}, Middle Value: {val}")