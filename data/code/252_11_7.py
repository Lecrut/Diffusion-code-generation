import math
def compare_quantities(a: float, b: float) -> tuple[float, float, float]:
    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    difference = abs(a - b)
    return larger, smaller, difference
if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.25
    larger, smaller, diff = compare_quantities(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Larger number: {larger}")
    print(f"Smaller number: {smaller}")
    print(f"Absolute difference: {diff}")
    num3 = -5.0
    num4 = -10.5
    larger2, smaller2, diff2 = compare_quantities(num3, num4)
    print(f"\nNumber 3: {num3}")
    print(f"Number 4: {num4}")
    print(f"Larger number: {larger2}")
    print(f"Smaller number: {smaller2}")
    print(f"Absolute difference: {diff2}")
    num5 = 3.14159
    num6 = 3.14158
    larger3, smaller3, diff3 = compare_quantities(num5, num6)
    print(f"\nNumber 5: {num5}")
    print(f"Number 6: {num6}")
    print(f"Larger number: {larger3}")
    print(f"Smaller number: {smaller3}")
    print(f"Absolute difference: {diff3}")