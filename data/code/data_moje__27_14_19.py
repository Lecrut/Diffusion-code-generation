def validate_triangle(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0

def format_result(side_a: float, side_b: float, side_c: float, is_valid: bool) -> str:
    status = "Valid" if is_valid else "Invalid"
    return f"Sides ({side_a}, {side_b}, {side_c}) form a {status} triangle."

if __name__ == '__main__':
    sample_a = 3.0
    sample_b = 4.0
    sample_c = 5.0
    result = validate_triangle(sample_a, sample_b, sample_c)
    formatted_output = format_result(sample_a, sample_b, sample_c, result)
    print(formatted_output)