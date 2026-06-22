def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

def calculate_ratio(a, b):
    return a / b

if __name__ == '__main__':
    try:
        ratio_a1 = 10
        ratio_b1 = 4
        validate_numbers(ratio_a1, ratio_b1)
        result1 = calculate_ratio(ratio_a1, ratio_b1)
        print(f"Ratio: {result1}")
    except (ValueError, ZeroDivisionError) as e:
        print(e)