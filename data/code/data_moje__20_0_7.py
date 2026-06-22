EVEN_MODULUS = 2

def is_even(number: int) -> bool:
    return number % EVEN_MODULUS == 0

if __name__ == '__main__':
    test_cases = [10, 13, -22, 0, 101]
    for value in test_cases:
        print(is_even(value))