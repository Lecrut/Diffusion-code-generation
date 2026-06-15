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
    num2 = 8.33
    larger, smaller, diff = compare_quantities(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Larger: {larger}")
    print(f"Smaller: {smaller}")
    print(f"Difference: {diff}")
    num3 = -5.0
    num4 = -10.5
    larger, smaller, diff = compare_quantities(num3, num4)
    print(f"\nNumber 3: {num3}")
    print(f"Number 4: {num4}")
    print(f"Larger: {larger}")
    print(f"Smaller: {smaller}")
    print(f"Difference: {diff}")
    num5 = 3.14159
    num6 = 3.14158
    larger, smaller, diff = compare_quantities(num5, num6)
    print(f"\nNumber 5: {num5}")
    print(f"Number 6: {num6}")
    print(f"Larger: {larger}")
    print(f"Smaller: {smaller}")
    print(f"Difference: {diff}")