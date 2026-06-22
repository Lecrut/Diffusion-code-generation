def find_middle(arr):
    n = len(arr)
    if n == 0:
        raise ValueError("Array is empty")
    mid_index = n // 2
    mid_value = arr[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [5],
        [1, 2, 3, 4],
        [100, 200, 300, 400, 500, 600]
    ]
    for arr in test_cases:
        idx, val = find_middle(arr)
        print(f"Array: {arr}, Middle Index: {idx}, Middle Value: {val}")