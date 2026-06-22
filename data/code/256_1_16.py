def validate_input(numbers):
    if not numbers:
        raise ValueError("Input list must contain at least one number")

def calculate_range(numbers):
    validate_input(numbers)
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return max_val - min_val

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = calculate_range(sample_list)
    print(result)