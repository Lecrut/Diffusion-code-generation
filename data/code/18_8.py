def get_middle_value(arr):
    if not arr:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = get_middle_value(sample_data)
    print(result)