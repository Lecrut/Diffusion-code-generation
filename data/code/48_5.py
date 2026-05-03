import math
def calculate_heron_area(sides):
    if len(sides) != 3:
        raise ValueError("Heron's formula requires exactly three side lengths.")
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The side lengths cannot form a valid triangle (Triangle Inequality Theorem or non-positive lengths).")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    sample_sides_valid = [3, 4, 5]
    sample_sides_invalid_triangle = [1, 2, 10]
    sample_sides_zero = [0, 4, 5]
    sample_sides_too_few = [3, 4]
    print(f"Sides {sample_sides_valid}: Area = {calculate_heron_area(sample_sides_valid)}")
    try:
        calculate_heron_area(sample_sides_invalid_triangle)
    except ValueError as e:
        print(f"Error for {sample_sides_invalid_triangle}: {e}")
    try:
        calculate_heron_area(sample_sides_zero)
    except ValueError as e:
        print(f"Error for {sample_sides_zero}: {e}")
    try:
        calculate_heron_area(sample_sides_too_few)
    except ValueError as e:
        print(f"Error for {sample_sides_too_few}: {e}")