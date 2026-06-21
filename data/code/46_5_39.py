def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_a = 7.1
    sample_b = 8.2
    sample_c = 9.3
    try:
        perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
        print(perimeter)
    except ValueError as e:
        print(e)