import math

def determine_larger(a, b, tolerance=1e-9):
    if math.isclose(a, b, rel_tol=tolerance):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    larger_value = determine_larger(num1, num2, tolerance=1e-9)
    print(larger_value)

    num3 = 1.0000000001
    num4 = 1.0
    larger_value = determine_larger(num3, num4, tolerance=1e-8)
    print(larger_value)