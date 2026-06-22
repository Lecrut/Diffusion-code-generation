def find_max_with_custom_logic(numbers):
    if not numbers:
        raise ValueError("Array must not be empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    hard_coded_array = [3.14, 2.71, 1.41, 9.8, 0.577, 4.67]
    result = find_max_with_custom_logic(hard_coded_array)
    print(result)