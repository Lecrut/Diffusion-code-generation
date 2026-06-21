EVEN_MODULUS = 2

def is_even(n):
    return n % EVEN_MODULUS == 0

if __name__ == '__main__':
    test_values = [10, 15, 20, 25, 30]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")