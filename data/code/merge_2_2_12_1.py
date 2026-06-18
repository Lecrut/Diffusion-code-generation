import cmath
def is_integer(value):
    return isinstance(value, int) and not isinstance(value, bool)
def is_float(value):
    return isinstance(value, float) and not isinstance(value, bool)
def check_positivity_int(n: int) -> bool:
    if n <= 0:
        raise TypeError("Input must be a positive integer.")
    return True
def check_positivity_float(x: float) -> bool:
    if x <= 0.0:
        raise ValueError("Float input is not strictly positive.")
    return True
def check_complex_real_positive(z: complex) -> bool:
    real_part = z.real
    if isinstance(real_part, int):
        pass
    elif isinstance(real_part, float):
        pass
    else:
        try:
            real_part = float(real_part)
        except (TypeError, ValueError):
            raise TypeError("Complex number's real part must be numeric.")
    if real_part <= 0.0:
        raise ValueError(f"Real part of complex {z} is not positive ({real_part}).")
    return True
if __name__ == '__main__':
    try:
        check_positivity_int(5)
        print("Integer 5 passed.")
    except Exception as e:
        print(f"Error testing integer 5: {e}")
    try:
        check_positivity_int(-3)
        print("Integer -3 should have failed but did not.")
    except TypeError as e:
        print(f"Correctly caught error for negative int: {e}")
    try:
        check_positivity_float(2.5)
        print("Float 2.5 passed.")
    except Exception as e:
        print(f"Error testing float 2.5: {e}")
    try:
        check_positivity_float(-10.7)
        print("Float -10.7 should have failed but did not.")
    except ValueError as e:
        print(f"Correctly caught error for negative float: {e}")
    try:
        check_complex_real_positive(3 + 4j)
        print("Complex 3+4i passed.")
    except Exception as e:
        print(f"Error testing complex 3+4i: {e}")
    try:
        check_complex_real_positive(-1.5 - 2.0j)
        print("Complex -1.5-2i should have failed but did not.")
    except ValueError as e:
        print(f"Correctly caught error for complex with negative real part: {e}")
    try:
        check_complex_real_positive(0 + 3j)
        print("Complex 0+3i should have failed but did not.")
    except ValueError as e:
        print(f"Correctly caught error for complex with zero real part: {e}")