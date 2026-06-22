def filter_odd_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    return [num for num in numbers if isinstance(num, int) and num % 2 != 0]

if __name__ == '__main__':
    sample_values = [10, 21, 32, 43, 54, 65]
    try:
        odd_numbers = filter_odd_numbers(sample_values)
        print(odd_numbers)
    except ValueError as e:
        print(e)