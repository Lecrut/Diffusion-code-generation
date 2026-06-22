def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if a >= b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    difference = abs(a - b)
    return f"Number 1: {a}, Number 2: {b}, Larger: {larger}, Smaller: {smaller}, Difference: {difference}"

if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.75
    result = compare_two_simple_quantities_now_format_results(num1, num2)
    print(result)