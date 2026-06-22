def filter_even_greater_than_ten(numbers):
    return {n for n in numbers if n > 10 and n % 2 == 0}

if __name__ == '__main__':
    sample_numbers = {5, 12, 3, 18, 7, 24}
    print(filter_even_greater_than_ten(sample_numbers))