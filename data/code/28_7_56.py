def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def is_larger(a, b):
    validate_numbers(a, b)
    return a > b

if __name__ == '__main__':
    print(is_larger(15, 10))
    print(is_larger(2, 8))
    print(is_larger(-3, -4))
    print(is_larger(7.5, 7.5))