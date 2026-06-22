def filter_odd_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    return [num for num in numbers if isinstance(num, int) and num % 2 != 0]

if __name__ == '__main__':
    sample_list = [17, 42, 5, 8, 33, 0, -7]
    try:
        odd_numbers = filter_odd_numbers(sample_list)
        print(odd_numbers)
    except Exception as e:
        print(f"Error: {e}")