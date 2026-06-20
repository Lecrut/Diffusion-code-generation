MAX_RETRIES = 5
MIN_VALUE = 0

def validate_integer(input_value):
    return isinstance(input_value, int) and input_value >= MIN_VALUE

def check_complex_condition(a, b, c):
    if not all((validate_integer(x) for x in [a, b, c])):
        raise ValueError('All inputs must be non-negative integers')
    if a > MAX_RETRIES or b > MAX_RETRIES or c > MAX_RETRIES:
        return False
    return (a + b) % 2 == 0 and c >= a
if __name__ == '__main__':
    sample_cases = [(3, 4, 5), (5, 2, 6), (1, 3, 7), (-1, 2, 3), (6, 0, 1)]
    for a, b, c in sample_cases:
        try:
            result = check_complex_condition(a, b, c)
            print(f'check_complex_condition({a}, {b}, {c}) = {result}')
        except ValueError as e:
            print(e)