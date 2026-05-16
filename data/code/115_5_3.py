def calculate_quotient(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    return dividend / divisor
if __name__ == '__main__':
    a = 10
    b = 2
    print(f"Quotient of {a} and {b}: {calculate_quotient(a, b)}")
    c = 15
    d = 3
    print(f"Quotient of {c} and {d}: {calculate_quotient(c, d)}")
    e = 7
    f = 0
    try:
        calculate_quotient(e, f)
    except ValueError as err:
        print(f"Error caught: {err}")