def find_middle_index_and_value(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    mid_index = len(arr) // 2
    mid_value = arr[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5, 7, 9],
        [10, 20, 30, 40, 50, 60],
        [42],
        [100, 200, 300, 400]
    ]
    for test in test_cases:
        index, value = find_middle_index_and_value(test)
        print(f"Array: {test}, Middle Index: {index}, Value: {value}")