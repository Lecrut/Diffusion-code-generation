def is_integer(x):
    return isinstance(x, int) and not isinstance(x, bool)
def is_float(x):
    return isinstance(x, float)
def has_positive_real_part(x):
    if hasattr(x, 'real'):
        return x.real > 0
    elif isinstance(x, (int, float)):
        return x > 0
    else:
        try:
            num = complex(x).real
            return num > 0
        except TypeError:
            return False
if __name__ == '__main__':
    test_cases_int = [1, -5, 0]
    print(f"Integer tests: {[(val, is_integer(val)) for val in test_cases_int]}")
    test_cases_float = [3.14, -2.7, 0.0]
    print(f"Float tests: {[(val, is_float(val)) for val in test_cases_float]}")
    complex_tests = [(1+2j), (-1-2j), (0+5j)]
    print(f"Complex real part tests: {[(z, has_positive_real_part(z)) for z in complex_tests]}")