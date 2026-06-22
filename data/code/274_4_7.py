def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11, 12]
    even_numbers = filter_even_numbers(sample_list)
    print(even_numbers)