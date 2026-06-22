def validate_input(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an integer or a float")

def is_positive(x):
    validate_input(x)
    return x > 0

if __name__ == '__main__':
    print(is_positive(7))
    print(is_positive(-2))
    print(is_positive(0))