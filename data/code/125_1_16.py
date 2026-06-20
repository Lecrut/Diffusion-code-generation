def arithmetic_operations(numbers):
    result_add = sum(numbers)
    result_subtract = numbers[0] - sum(numbers[1:])
    return result_add, result_subtract

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    add_result, subtract_result = arithmetic_operations(sample_numbers)
    print("Addition Result:", add_result)
    print("Subtraction Result:", subtract_result)