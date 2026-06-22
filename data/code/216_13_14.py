def middle_value(arr):
    length = len(arr)
    if length == 0:
        return None
    index = length // 2
    return arr[index]

if __name__ == '__main__':
    sample = [100, 200, 300]
    print(middle_value(sample))