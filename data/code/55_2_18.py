def calculate_triangle_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sides do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)