def arithmetic_operations(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
        else:
            result -= abs(number)
    return result

if __name__ == '__main__':
    test_numbers = [10, -5, 3, -2]
    print(arithmetic_operations(test_numbers))