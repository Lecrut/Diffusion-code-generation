def verify_triangle_inequality(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sample_values = [(3, 4, 5), (1, 2, 3), (0.5, 0.5, 0.8), (10, 2, 1), (7, 7, 7)]
    for a, b, c in sample_values:
        result = verify_triangle_inequality(a, b, c)
        print(result)