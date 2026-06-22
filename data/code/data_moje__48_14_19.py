def find_max_custom(arr):
    if not arr:
        return None
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    data = [1.5, 3.2, 0.9, 7.4, 2.1]
    result = find_max_custom(data)
    print(result)