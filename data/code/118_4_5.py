from functools import mul

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return mul(a, b)

if __name__ == '__main__':
    print(multiply(4, 3))