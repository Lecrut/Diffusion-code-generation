def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_values = [15, 22, 37, 48, 59, 60]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)