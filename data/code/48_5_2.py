import math
def calculate_heron_area(sides):
    if len(sides) != 3:
        raise ValueError("Heron's formula requires exactly three side lengths.")
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The side lengths do not form a valid triangle.")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    sample_sides_valid = [3, 4, 5]
    sample_sides_invalid_triangle = [1, 2, 10]
    sample_sides_invalid_length = [3, 4, -5]
    sample_sides_too_few = [3, 4]
    print(f"Sides: {sample_sides_valid}")
    try:
        area1 = calculate_heron_area(sample_sides_valid)
        print(f"Area: {area1}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    print(f"Sides: {sample_sides_invalid_triangle}")
    try:
        area2 = calculate_heron_area(sample_sides_invalid_triangle)
        print(f"Area: {area2}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    print(f"Sides: {sample_sides_invalid_length}")
    try:
        area3 = calculate_heron_area(sample_sides_invalid_length)
        print(f"Area: {area3}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    print(f"Sides: {sample_sides_too_few}")
    try:
        area4 = calculate_heron_area(sample_sides_too_few)
        print(f"Area: {area4}")
    except ValueError as e:
        print(f"Error: {e}")