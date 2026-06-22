def get_middle_value(arr):
    if not arr:
        return None
    index = len(arr) // 2
    return arr[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_data)
    print(result)