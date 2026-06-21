def find_median(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        middle1, middle2 = sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
        return (middle1 + middle2) / 2.0

if __name__ == '__main__':
    sample_input_str = "3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5"
    try:
        input_list = [int(x.strip()) for x in sample_input_str.split(',')]
        middle_value = find_median(input_list)
        print(f"The median value is: {middle_value}")
    except ValueError as e:
        print(e)