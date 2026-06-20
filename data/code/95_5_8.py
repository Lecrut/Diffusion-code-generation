def is_positive(x):
    return x > 0

def is_even(x):
    return x % 2 == 0

def is_divisible(a, c):
    return c % a == 0 if a != 0 else False

def check_integers(a, b, c):
    return (is_positive(a), is_even(b), is_divisible(a, c))

if __name__ == '__main__':
    result = check_integers(8, 15, 40)
    print(result)