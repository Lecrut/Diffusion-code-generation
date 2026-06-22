def find_middle_index_and_value(arr):
    if not arr:
        return None, None
    length = len(arr)
    middle_index = length // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [100],
        [],
        [5, 10, 15, 20, 25, 30]
    ]
    for arr in test_cases:
        idx, val = find_middle_index_and_value(arr)
        print(f"Array: {arr}, Middle Index: {idx}, Middle Value: {val}")