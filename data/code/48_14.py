def find_custom_max(numbers):
    if not numbers:
        raise ValueError("Array must not be empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    hard_coded_array = [3.14, 2.71, 1.618, 9.81, 0.577, 4.2, 7.5]
    result = find_custom_max(hard_coded_array)
    print(result)