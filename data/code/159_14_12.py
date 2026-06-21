def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 11, 13, 15]
    result = filter_odd_numbers(sample_values)
    print(result)