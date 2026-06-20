from typing import Tuple

def compute_results(a: int, b: int) -> Tuple[int, float]:
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None
    return sum_result, difference_result, product_result, quotient_result

if __name__ == '__main__':
    a = 100
    b = 7
    results = compute_results(a, b)
    print(f"Sum: {results[0]}")
    print(f"Difference: {results[1]}")
    print(f"Product: {results[2]}")
    if results[3] is not None:
        print(f"Quotient: {results[3]}")
    else:
        print("Cannot compute quotient as b is 0.")