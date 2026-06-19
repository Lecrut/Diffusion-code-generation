def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "All sides must be numeric types."
    if any(x <= 0 for x in [a, b, c]):
        return "Side lengths must be positive numbers."
    return a + b + c

if __name__ == '__main__':
    sample_values = [(3, 4, 5), (7.5, 9.2, 4.8), ('a', 4, 5), (-3, 4, 5)]
    for values in sample_values:
        result = calculate_triangle_perimeter(*values)
        print(result)