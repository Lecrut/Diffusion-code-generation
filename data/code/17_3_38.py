def get_even_numbers(numbers):
    return [num for num in numbers if not num % 2]

if __name__ == '__main__':
    test_values = [15, 22, 37, 40, 55, 68, 79, 82, 93, 104]
    even_numbers = get_even_numbers(test_values)
    print(even_numbers)