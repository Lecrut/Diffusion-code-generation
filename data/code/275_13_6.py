def filter_even_numbers(numbers):
    return {num for num in numbers if num > 10 and num % 2 == 0}

if __name__ == '__main__':
    sample_values = {5, 12, 3, 8, 14, 17}
    print(filter_even_numbers(sample_values))