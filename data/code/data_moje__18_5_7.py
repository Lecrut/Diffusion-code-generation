def find_middle_index_and_value(arr):
    if not arr:
        raise ValueError('Array must not be empty')
    n = len(arr)
    middle_index = n // 2
    if n % 2 == 0:
        middle_index = middle_index - 1
    middle_value = arr[middle_index]
    return (middle_index, middle_value)
if __name__ == '__main__':
    test_cases = [[1, 2, 3, 4, 5], [10, 20, 30, 40], [7], [1, 2], [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [100, 200, 300, 400, 500, 600]]
    for arr in test_cases:
        middle_idx, middle_val = find_middle_index_and_value(arr)
        print(f'Array: {arr}')
        print(f'Middle Index: {middle_idx}, Middle Value: {middle_val}')
        print()