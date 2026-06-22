def compute_ellipse_area(a: float, b: float) -> float:
    return 3.14159265358979323846 * a * b

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    result = compute_ellipse_area(a, b)
    print(result)