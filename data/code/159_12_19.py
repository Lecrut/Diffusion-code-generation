def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    sample_values = [10, 15, 20, 25, 30, 35]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)