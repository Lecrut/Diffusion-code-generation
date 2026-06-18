import cmath
def is_integer(value):
    return isinstance(value, int) and not isinstance(value, bool)
def is_float(value):
    return isinstance(value, float) and not isinstance(value, bool)
def check_positivity_int(n: int) -> bool:
    if n <= 0:
        raise ValueError("Integer must be positive")
    return True
def check_positivity_float(x: float) -> bool:
    if x <= 0.0:
        raise ValueError("Float must be strictly greater than zero")
    return True
def check_complex_real_positive(z: complex) -> bool:
    real_part = z.real
    if isinstance(real_part, int):
        if not is_integer(real_part):
            pass                                                                                      
        elif real_part <= 0.0:
            raise ValueError("Real part must be positive")
    else:
        if real_part <= 0.0:
            raise ValueError("Real part must be strictly greater than zero")
    return True
def validate_and_check(value):
    if isinstance(value, int) and not isinstance(value, bool):
        check_positivity_int(value)
    elif isinstance(value, float):
        check_positivity_float(value)
    elif isinstance(value, complex):
        check_complex_real_positive(value)
    else:
        raise TypeError(f"Unsupported type for positivity test: {type(value)}")
if __name__ == '__main__':
    samples = [10, 5.7, -3, cmath.rect(2, 0), complex(-4, 9)]
    results = []
    for val in samples:
        try:
            validate_and_check(val)
            result_str = f"Validated successfully (Type: {type(val).__name__})"
        except ValueError as e:
            result_str = f"Validation failed: {e}"
        except TypeError as e:
            result_str = f"TypeError: {e}"
        results.append((val, result_str))
    for val, res in results:
        print(f"{res}")