def filter_even_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 72, 91]
    try:
        even_numbers = filter_even_numbers(sample_numbers)
        print(even_numbers)
    except ValueError as e:
        print(e)