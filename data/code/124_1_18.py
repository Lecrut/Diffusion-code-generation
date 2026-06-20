def basic_arithmetic(a, b):
    addition_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    floor_division_result = a // b
    return {
        'addition': addition_result,
        'subtraction': subtraction_result,
        'multiplication': multiplication_result,
        'floor_division': floor_division_result
    }

if __name__ == '__main__':
    sample_a = 20
    sample_b = 5
    result = basic_arithmetic(sample_a, sample_b)
    print(result)