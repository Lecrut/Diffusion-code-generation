import math

def find_larger_or_closest(a, b, tolerance=1e-9):
    if math.isclose(a, b, rel_tol=tolerance):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    num1 = 0.3
    num2 = 0.1 + 0.2
    result = find_larger_or_closest(num1, num2, tolerance=1e-9)
    print(result)