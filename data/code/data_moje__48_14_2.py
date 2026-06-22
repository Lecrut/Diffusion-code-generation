def find_max_custom(numbers):
    if not numbers:
        raise ValueError("Array cannot be empty")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_array = [3.5, 7.2, 1.8, 9.4, 6.1]
    print(find_max_custom(sample_array))