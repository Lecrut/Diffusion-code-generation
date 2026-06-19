def get_perimeter(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    return a + b + c

if __name__ == '__main__':
    triangle_sides1 = (6, 8, 10)
    try:
        perimeter1 = get_perimeter(triangle_sides1)
        print(f"Perimeter of {triangle_sides1}: {perimeter1}")
    except ValueError as e:
        print(f"Error: {e}")

    triangle_sides2 = (7, 24, 25)
    try:
        perimeter2 = get_perimeter(triangle_sides2)
        print(f"Perimeter of {triangle_sides2}: {perimeter2}")
    except ValueError as e:
        print(f"Error: {e}")