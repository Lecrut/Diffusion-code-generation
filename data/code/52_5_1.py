def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values.")
    return 0.5 * base * height
if __name__ == '__main__':
    base1 = 10
    height1 = 5
    try:
        area1 = calculate_triangle_area(base1, height1)
        print(f"Area with base={base1} and height={height1}: {area1}")
    except ValueError as e:
        print(f"Error: {e}")
    base2 = 0
    height2 = 4
    try:
        area2 = calculate_triangle_area(base2, height2)
        print(f"Area with base={base2} and height={height2}: {area2}")
    except ValueError as e:
        print(f"Error: {e}")
    base3 = 7.5
    height3 = 8
    try:
        area3 = calculate_triangle_area(base3, height3)
        print(f"Area with base={base3} and height={height3}: {area3}")
    except ValueError as e:
        print(f"Error: {e}")