def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if a >= b:
        larger = f"Number 1: {a}"
        smaller = f"Number 2: {b}"
    else:
        larger = f"Number 1: {b}"
        smaller = f"Number 2: {a}"
    difference = abs(a - b)
    return f"{larger}\n{smaller}\nDifference: {difference:.2f}"

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_format_results(15.75, 8.25)
    print(result)