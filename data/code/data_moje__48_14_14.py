def find_max_custom(arr):
    if not arr:
        return None
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

if __name__ == '__main__':
    numbers = [3.14, 1.41, 2.72, 1.61, 0.58]
    result = find_max_custom(numbers)
    print(result)