def filter_even_numbers(numbers):
    return {num for num in numbers if num > 10 and num % 2 == 0}

if __name__ == '__main__':
    sample_numbers = {8, 15, 20, 7, 12}
    result = filter_even_numbers(sample_numbers)
    print(result)