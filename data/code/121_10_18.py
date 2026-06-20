import math

TOLERANCE = 1e-9

def compare_and_return_larger(a, b):
    if math.isclose(a, b, rel_tol=TOLERANCE):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    result = compare_and_return_larger(0.1 + 0.2, 0.3, tolerance=1e-9)
    print(result)