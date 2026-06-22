def get_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    test_values = [15, 22, 37, 48, 53, 60, 79, 82, 91, 100]
    odd_numbers = get_odd_numbers(test_values)
    print(odd_numbers)