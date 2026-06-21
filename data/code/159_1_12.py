def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 4, 7, 9, 12, 15]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)