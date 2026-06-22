def validate_quantity(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    validate_quantity(a)
    validate_quantity(b)

    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a

    difference = abs(a - b)

    return f"Larger quantity: {larger}, Smaller quantity: {smaller}, Difference: {difference}"

if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.25
    result = compare_two_simple_quantities_now_format_results(num1, num2)
    print(result)