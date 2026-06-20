def validate_inputs(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or (not isinstance(c, int)):
        raise ValueError('All inputs must be integers.')
    if a <= 0:
        raise ValueError('The first input must be positive.')

def combine_conditions(a, b, c):
    check_a_positive = a > 0
    check_b_even = b % 2 == 0
    check_c_divisible_by_a = a != 0 and c % a == 0
    return check_a_positive and check_b_even and check_c_divisible_by_a
if __name__ == '__main__':
    try:
        print(f'Test 1 (a=2, b=4, c=6): {combine_conditions(2, 4, 6)}')
        print(f'Test 2 (a=3, b=5, c=7): {combine_conditions(3, 5, 7)}')
        print(f'Test 3 (a=-1, b=2, c=4): {combine_conditions(-1, 2, 4)}')
    except ValueError as e:
        print(e)