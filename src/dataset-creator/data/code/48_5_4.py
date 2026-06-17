import math
def advanced_divide(a: float | int, b: float | int) -> dict[str, any]:
    if not isinstance(b, (int, float)) and b != 0:
        raise TypeError("Second argument must be numeric.")
    result = a / b
    return {
        "dividend": type(a).__name__,
        "divisor": type(b).__name__,
        "quotient": round(result, 6),
        "remainder": float(0) if isinstance(a, int) else math.modf(result)[1] * abs(b),
        "is_exact_division": result.is_integer() and b != 0 or a % b == 0 if isinstance(a, (int, float)) else False
    }
if __name__ == '__main__':
    sample_data = {
        ("integer", "float"): (10, 3.5),
        ("float", "int"): (42.7, 6),
        ("negative_int", "positive_float"): (-8, 2.0)
    }
    for label, values in sample_data.items():
        a, b = values
        output = advanced_divide(a, b)
        print(f"Label: {label}")
        print(output)