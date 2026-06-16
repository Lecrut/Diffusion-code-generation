import cmath
def is_integer(value):
    return isinstance(value, int) and not isinstance(value, bool)
def is_float(value):
    return isinstance(value, float) and not isinstance(value, bool)
def check_positivity_int(n: int) -> bool:
    if n > 0:
        return True
    elif n == 0:
        return False
    else:
        raise ValueError("Input must be non-negative integer")
def check_positivity_float(x: float, tolerance=1e-9) -> bool:
    return x > -tolerance and not (abs(x) < tolerance)
def check_complex_part(z: complex) -> bool:
    real_part = z.real
    if isinstance(real_part, int):
        return is_integer(real_part)
    elif isinstance(real_part, float):
        return check_positivity_float(float(real_part))
    else:
        raise TypeError("Real part must be numeric")
def main():
    test_ints = [0, 1, -5]
    for val in test_ints:
        try:
            result = check_positivity_int(val)
            print(f"Integer {val}: Positive={result}")
        except ValueError as e:
            print(f"Integer {val}: Error-{e}")
    test_floats = [0.5, -1.234, 1e-10]
    for val in test_floats:
        result = check_positivity_float(val)
        print(f"Float {val}: Positive={result}")
    complex_nums = [(1+2j), (-3+4j), (5j)]
    for z in complex_nums:
        try:
            is_positive_real = check_complex_part(z)
            print(f"Complex {z} Real Part Positive={is_positive_real}")
        except TypeError as e:
            print(f"Complex {z}: Error-{e}")
if __name__ == '__main__':
    main()