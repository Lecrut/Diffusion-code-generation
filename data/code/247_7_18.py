CONSTANT_A = 5
CONSTANT_B = 3

def add_constants(a=CONSTANT_A, b=CONSTANT_B):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    try:
        result = add_constants()
        print(result)
    except ValueError as e:
        print(e)