def is_positive_even_and_lt_100(n):
    return n > 0 and n % 2 == 0 and n < 100

def validate_input(a, b, c):
    return all(is_positive_even_and_lt_100(x) for x in (a, b, c))

if __name__ == '__main__':
    print(validate_input(4, 68, 98))
    print(validate_input(100, 20, 30))
    print(validate_input(5, 10, 100))
    print(validate_input(4, 6, 8))
    print(validate_input(10, 21, 30))