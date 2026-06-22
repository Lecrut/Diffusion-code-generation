EXPONENT = 8
BASE_VALUE = 3

def compute_exponentiation(base, exponent):
    return base ** exponent

if __name__ == '__main__':
    calculated = compute_exponentiation(BASE_VALUE, EXPONENT)
    print(calculated)