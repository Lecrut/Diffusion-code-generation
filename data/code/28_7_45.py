def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both arguments must be numbers')

def is_larger(a, b):
    validate_numbers(a, b)
    return a > b
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(3, 7))
    print(is_larger(-1, -2))
    print(is_larger(0, 0))