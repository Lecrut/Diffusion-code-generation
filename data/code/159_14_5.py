def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7]
    print(filter_odd_numbers(sample_values))