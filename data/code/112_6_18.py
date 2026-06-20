def validate_inputs(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric.")

def add_numbers(a, b):
    try:
        validate_inputs(a, b)
        return a + b
    except TypeError as e:
        print(e)

if __name__ == '__main__':
    print(add_numbers(5, 10))
    print(add_numbers(3.5, 7))
    print(add_numbers("hello", 10))