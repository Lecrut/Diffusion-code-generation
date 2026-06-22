def is_integer(value):
    return isinstance(value, int)

def compare_numbers(a, b):
    if not (is_integer(a) and is_integer(b)):
        raise ValueError("Both arguments must be integers")
    return a > b

if __name__ == '__main__':
    print(compare_numbers(10, 5))
    print(compare_numbers(20, 30))
    print(compare_numbers(7, 7))
    print(compare_numbers(-5, 12))
    print(compare_numbers(0, -1))