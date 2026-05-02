import math
def simplify_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    common = math.gcd(a, b)
    return a // common, b // common
if __name__ == '__main__':
    ratio1 = 12
    ratio2 = 18
    try:
        num1, den1 = simplify_ratio(ratio1, ratio2)
        print(f"Simplified ratio for {ratio1}:{ratio2} is {num1}:{den1}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")