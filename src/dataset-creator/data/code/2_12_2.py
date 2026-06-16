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
def check_complex_part_positive(z: complex, part_name="real"):
    real_val = z.real
    imag_val = z.imag
    if isinstance(part_name, str):
        target_value = real_val if part_name.lower() == "real" else imag_val
        if target_value <= 0.0:
            raise ValueError(f"{part_name.capitalize()} part of complex number must be positive")
    return True
if __name__ == '__main__':
    test_cases_int = [1, -5, 0]
    for val in test_cases_int:
        try:
            check_positivity_int(val)
            print(f"Integer {val}: Passed (should have raised error)")
        except ValueError as e:
            print(f"Integer {val}: Correctly failed with '{e}'")
    test_cases_float = [3.14, -2.5, 0.0]
    for val in test_cases_float:
        try:
            check_positivity_float(val)
            print(f"Float {val}: Passed (should have raised error)")
        except ValueError as e:
            print(f"Float {val}: Correctly failed with '{e}'")
    complex_tests = [complex(5, 2), complex(-3.0, -4)]
    for val in complex_tests:
        try:
            check_complex_part_positive(val)
            print(f"Complex {val}: Passed (should have raised error)")
        except ValueError as e:
            print(f"Complex {val}: Correctly failed with '{e}'")
    valid_int = 42
    if is_integer(valid_int):
        print("Integer type check passed.")
    valid_float = 3.14
    if is_float(valid_float):
        print("Float type check passed.")