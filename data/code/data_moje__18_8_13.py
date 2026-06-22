def get_middle_value(arr):
    if len(arr) == 0:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_data)
    print(result)