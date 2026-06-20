import math

def compare_and_max(x, y, tolerance=1e-09):
    if math.isclose(x, y, rel_tol=tolerance):
        return max(x, y)
    else:
        return None
if __name__ == '__main__':
    result = compare_and_max(0.1 + 0.2, 0.3, tolerance=1e-09)
    print(result)