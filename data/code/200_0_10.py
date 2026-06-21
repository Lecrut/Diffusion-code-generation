def filter_even_numbers(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return even_numbers

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(sample_numbers)
    print(result)