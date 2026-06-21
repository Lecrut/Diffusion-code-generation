def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 72, 91]
    even_numbers = filter_even_numbers(sample_numbers)
    print(even_numbers)