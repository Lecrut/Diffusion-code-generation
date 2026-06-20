import math

def compare_and_return_larger(a, b, tolerance=1e-9):
    if math.isclose(a, b, rel_tol=tolerance):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    result = compare_and_return_larger(num1, num2, tolerance=1e-9)
    print(result)

    num3 = 1.000000001
    num4 = 1.0
    result = compare_and_return_larger(num3, num4, tolerance=1e-9)
    print(result)

    num5 = -0.1 + 0.2
    num6 = 0.1
    result = compare_and_return_larger(num5, num6, tolerance=1e-9)
    print(result)