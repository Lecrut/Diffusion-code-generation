BASE = 2
EXPONENT = 10

def binary_exponentiation(base=BASE, exponent=EXPONENT):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(binary_exponentiation())