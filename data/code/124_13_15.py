def validate_numbers(a: float, b: float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Second number cannot be zero")

def perform_operations(a: float, b: float) -> tuple:
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    div_val = a / b
    return (sum_val, diff_val, prod_val, div_val)

if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.5
    validate_numbers(num1, num2)
    results = perform_operations(num1, num2)
    print(results)