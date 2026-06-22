def middle_value(arr):
    if not arr:
        return None
    length = len(arr)
    if length % 2 == 0:
        return (arr[length // 2 - 1] + arr[length // 2]) / 2
    else:
        return arr[length // 2]

if __name__ == '__main__':
    sample = [100, 200, 300]
    print(middle_value(sample))