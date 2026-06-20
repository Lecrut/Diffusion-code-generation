def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def is_less_than_100(num):
    return num < 100

def check_conditions(a, b, c):
    if is_positive(a) and is_even(a) and is_less_than_100(a):
        return is_positive(b) and is_even(b) and is_less_than_100(b) and is_positive(c) and is_even(c) and is_less_than_100(c)
    return False

if __name__ == '__main__':
    print(check_conditions(2, 4, 6))
    print(check_conditions(-2, 4, 6))
    print(check_conditions(2, -4, 6))
    print(check_conditions(2, 4, 102))