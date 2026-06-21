def get_even_numbers(numbers):
    return [num for num in numbers if not num % 2]

if __name__ == '__main__':
    test_values = [15, 22, 37, 48, 55, 60, 79, 82, 91, 100]
    even_numbers = get_even_numbers(test_values)
    print(even_numbers)