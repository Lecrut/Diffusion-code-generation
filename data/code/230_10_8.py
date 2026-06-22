def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)