def get_middle_value(arr):
    length = len(arr)
    if length == 0:
        return None
    mid_index = length // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_array = [100, 200, 300]
    print(get_middle_value(sample_array))