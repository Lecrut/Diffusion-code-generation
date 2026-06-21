def get_middle_value(arr):
    if not arr:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    print(get_middle_value(test_data))