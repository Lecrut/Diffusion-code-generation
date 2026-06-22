def middle_value(arr):
    if not arr:
        return None
    length = len(arr)
    mid_index = length // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample = [100, 200, 300]
    print(middle_value(sample))