def compare_booleans(a: bool, b: bool) -> tuple:
    operation = '=='
    result = a == b
    return result, operation

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    comparison_result = compare_booleans(sample_a, sample_b)
    print(comparison_result)