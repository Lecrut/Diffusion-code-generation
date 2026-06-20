def arithmetic_operations(numbers):
    result_add = sum(numbers)
    result_subtract = numbers[0] - sum(numbers[1:])
    return result_add, result_subtract

if __name__ == '__main__':
    test_numbers = [5, 3, 8, 2]
    add_result, subtract_result = arithmetic_operations(test_numbers)
    print("Addition Result:", add_result)
    print("Subtraction Result:", subtract_result)