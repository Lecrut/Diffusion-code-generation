def filter_even_greater_than_ten(numbers):
    return {num for num in numbers if num > 10 and num % 2 == 0}

if __name__ == '__main__':
    sample_numbers = {5, 12, 3, 18, 7, 20}
    print(filter_even_greater_than_ten(sample_numbers))