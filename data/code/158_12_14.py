def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)