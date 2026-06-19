def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        return "All sides must be positive numbers"
    return a + b + c

if __name__ == '__main__':
    result = calculate_triangle_perimeter(5, 12, 13)
    print(result)