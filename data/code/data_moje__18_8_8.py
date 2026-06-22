def get_middle_value(arr):
    if not arr:
        return None
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5]
    result = get_middle_value(test_data)
    print(result)