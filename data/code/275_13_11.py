def filter_even_numbers(numbers):
    return {num for num in numbers if num > 10 and num % 2 == 0}

if __name__ == '__main__':
    sample_numbers = {5, 12, 3, 18, 7, 24}
    print(filter_even_numbers(sample_numbers))