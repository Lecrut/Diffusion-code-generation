def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_even_numbers(sample_values))