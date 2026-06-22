def validate_input(a: float, b: float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def format_quantity(quantity: float) -> str:
    return f"{quantity:.2f}"

def compare_two_simple_quantities_now_format_results(a: float, b: float) -> tuple[str, str, str]:
    validate_input(a, b)
    
    if a >= b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    
    difference = abs(a - b)
    
    return format_quantity(larger), format_quantity(smaller), format_quantity(difference)

if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.25
    larger, smaller, diff = compare_two_simple_quantities_now_format_results(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Larger: {larger}")
    print(f"Smaller: {smaller}")