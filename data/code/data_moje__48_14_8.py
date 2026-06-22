def find_max_custom(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    numbers = [3.14, 2.71, 1.41, 1.73, 0.57]
    result = find_max_custom(numbers)
    print(result)