def filter_odd(numbers):
    return [x for x in numbers if x % 2 != 0]

if __name__ == '__main__':
    sample_values = [10, 23, 36, 47, 58, 69]
    odd_numbers = filter_odd(sample_values)
    print(odd_numbers)