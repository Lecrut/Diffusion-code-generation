def filter_even_numbers(numbers):
    even_nums = {num for num in numbers if num > 10 and num % 2 == 0}
    return even_nums

if __name__ == '__main__':
    sample_numbers = {9, 16, 11, 3, 24, 5}
    result = filter_even_numbers(sample_numbers)
    print(result)