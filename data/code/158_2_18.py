def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_numbers = filter_even_numbers(sample_list)
    print(even_numbers)