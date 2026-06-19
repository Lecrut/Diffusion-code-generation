def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [10, 23, 36, 47, 58]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)