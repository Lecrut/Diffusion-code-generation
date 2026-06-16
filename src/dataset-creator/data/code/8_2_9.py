import math
def validate_and_process(value: float) -> str:
    if value < 0:
        return "Value is negative."
    elif value <= 10:
        result = f"Small positive ({value}). Squared: {math.pow(value, 2)}."
    else:
        result = f"Large positive ({value}). Cube root: {round(math.cbrt(value), 4)}."
    return result
def run_validation_tests() -> None:
    test_cases = [
        -5.0,
        3.14,
        25.789,
        100.0
    ]
    for val in test_cases:
        output = validate_and_process(val)
        print(f"Input: {val} -> Output: {output}")
if __name__ == '__main__':
    run_validation_tests()