def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        area1 = calculate_triangle_area(3, 4)
        print(f"Area for base 3, height 4: {area1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        area2 = calculate_triangle_area(5, 6)
        print(f"Area for base 5, height 6: {area2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        area3 = calculate_triangle_area(-1, 4)
        print(f"Area for base -1, height 4: {area3}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        area4 = calculate_triangle_area(3, 0)
        print(f"Area for base 3, height 0: {area4}")
    except ValueError as e:
        print(f"Error: {e}")