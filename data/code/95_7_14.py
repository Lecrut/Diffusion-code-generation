def validate_arguments(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError('All arguments must be integers')
    if a <= 0:
        raise ValueError('First argument must be positive')
    if b % 2 != 0:
        raise ValueError('Second argument must be even')

def combine_checks(a, b, c):
    validate_arguments(a, b, c)
    return c % (a * b) == 0
if __name__ == '__main__':
    print(f'Test 1 (a=2, b=4, c=8): {combine_checks(2, 4, 8)}')
    print(f'Test 2 (a=3, b=6, c=9): {combine_checks(3, 6, 9)}')
    print(f'Test 3 (a=-1, b=2, c=4): {combine_checks(-1, 2, 4)}')