def arithmetic_operations(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            if len(result) == 0:
                result += number
            else:
                result -= number
    return result

if __name__ == '__main__':
    test_numbers = [10, 5, 3]
    print(arithmetic_operations(test_numbers))