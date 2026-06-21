def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    sample_values = [11, 12, 13, 14, 15]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)