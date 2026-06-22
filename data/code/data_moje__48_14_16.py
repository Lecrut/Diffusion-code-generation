def find_max_custom(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_array = [3.14, 2.71, 1.61, 9.81, 0.57]
    result = find_max_custom(sample_array)
    print(result)