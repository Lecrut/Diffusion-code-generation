def arithmetic_operations(numbers):
    result_add = sum(numbers)
    result_subtract = numbers[0] - sum(numbers[1:])
    return result_add, result_subtract

if __name__ == '__main__':
    test_numbers = [5, 3, 9, 2]
    add_result, subtract_result = arithmetic_operations(test_numbers)
    print(f"Addition: {add_result}")
    print(f"Subtraction: {subtract_result}")