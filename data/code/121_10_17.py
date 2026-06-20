import math

def compare_and_return_larger(num1, num2, tolerance=1e-09):
    if math.isclose(num1, num2, rel_tol=tolerance):
        return max(num1, num2)
    else:
        return None
if __name__ == '__main__':
    result = compare_and_return_larger(0.1 + 0.2, 0.3, tolerance=1e-09)
    print(result)