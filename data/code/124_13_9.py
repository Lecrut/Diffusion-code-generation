def validate_inputs(a: float, b: float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Second input cannot be zero")

def perform_operations(a: float, b: float) -> tuple:
    validate_inputs(a, b)
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    div_val = a / b if b != 0 else None
    return (sum_val, diff_val, prod_val, div_val)

if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.5
    results = perform_operations(num1, num2)
    print(results)