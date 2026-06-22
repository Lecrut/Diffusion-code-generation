def compute_surface_area(a, b, c):
    return 2 * (a * b + b * c + c * a)

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    c = 2.0
    result = compute_surface_area(a, b, c)
    print(result)