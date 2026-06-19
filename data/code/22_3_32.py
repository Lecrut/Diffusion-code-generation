def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [10, 21, 32, 43, 54, 65]
    odd_numbers = filter_odd_numbers(sample_values)
    print("Odd numbers:", odd_numbers)