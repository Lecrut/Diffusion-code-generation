def filter_even_numbers(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements in the list must be integers.")
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        result = filter_even_numbers(sample_values)
        print(result)
    except ValueError as e:
        print(e)