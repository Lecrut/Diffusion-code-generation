def middle_value(arr):
    if len(arr) == 0:
        return None
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample = [100, 200, 300]
    print(middle_value(sample))