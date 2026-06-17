def multiply_integers(a: int | float = None, b: int | float = None) -> int:
    if a is not None and (not isinstance(a, int)):
        try:
            a = int(float(a))
        except ValueError:
            raise TypeError("Input 'a' must be convertible to an integer")
    elif a is None:
        a = 0
    if b is not None and (not isinstance(b, int)):
        try:
            b = int(float(b))
        except ValueError:
            raise TypeError("Input 'b' must be convertible to an integer")
    elif b is None:
        b = 0
    return a * b
if __name__ == '__main__':
    result_a = multiply_integers(15, "2.7")
    print(f"Result with string input: {result_a}")
    large_val = 9**38 + 42
    result_b = multiply_integers(large_val, -10)
    print(f"Large integer multiplication: {abs(result_b)}")