def arithmetic_operations(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, int) or isinstance(number, float):
            result += number
        else:
            raise ValueError("All elements must be numbers")
    return result

if __name__ == '__main__':
    test_numbers = [10, 20, 30, 40]
    print(arithmetic_operations(test_numbers))