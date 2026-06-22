def find_maximum_with_custom_logic(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.41, 9.81, 0.57, 1.62]
    result = find_maximum_with_custom_logic(sample_values)
    print(result)