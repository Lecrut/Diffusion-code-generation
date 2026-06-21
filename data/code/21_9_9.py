def _validate_integers(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise TypeError("All arguments must be integers")

def get_maximum_of_three(x, y, z):
    _validate_integers(x, y, z)
    current_max = x
    if y > current_max:
        current_max = y
    if z > current_max:
        current_max = z
    return current_max

if __name__ == '__main__':
    TEST_A = 45
    TEST_B = 92
    TEST_C = 33
    print(get_maximum_of_three(TEST_A, TEST_B, TEST_C))
    print(get_maximum_of_three(-8, -2, -15))
    print(get_maximum_of_three(0, 0, 0))