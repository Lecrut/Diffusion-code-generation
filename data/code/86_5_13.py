def compare_booleans(a: bool, b: bool) -> tuple:
    result = a == b
    operation = '=='
    return (result, operation)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = compare_booleans(sample_a, sample_b)
    print(result)