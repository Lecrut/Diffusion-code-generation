EVEN_MODULUS = 2

def is_even(n):
    return n % EVEN_MODULUS == 0

if __name__ == '__main__':
    test_values = [-15, -14, -13, -12, -11, 0, 11, 12, 13, 14, 15]
    even_results = {value: is_even(value) for value in test_values}
    print(even_results)