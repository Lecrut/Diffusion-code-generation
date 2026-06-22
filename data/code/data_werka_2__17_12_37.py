EVEN_CHECK_MODULO = 2

def is_even(n):
    return n % EVEN_CHECK_MODULO == 0

if __name__ == '__main__':
    test_values = [0, -1, -2, 3, 4, 5, 6]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")