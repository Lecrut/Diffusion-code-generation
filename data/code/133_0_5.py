def validate_input(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def compare_integers(a, b):
    validate_input(a, b)
    return a == b

if __name__ == '__main__':
    print(compare_integers(5, 5))  # True
    print(compare_integers(3, 4))  # False