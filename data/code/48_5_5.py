import math
def calculate_heron_area(side_lengths):
    if len(side_lengths) < 3:
        return None
    s = sum(side_lengths)
    if s % 2 != 0:
        return None
    s_half = s / 2
    if any(x <= 0 for x in side_lengths):
        return None
    try:
        area_squared = s_half * (s_half - side_lengths[0]) * (s_half - side_lengths[1]) * (s_half - side_lengths[2])
        a = side_lengths[0]
        b = side_lengths[1]
        c = side_lengths[2]
        s_triangle = a + b + c
        if s_triangle % 2 != 0:
            return None
        s_half_triangle = s_triangle / 2
        area_squared_triangle = s_half_triangle * (s_half_triangle - a) * (s_half_triangle - b) * (s_half_triangle - c)
        if area_squared_triangle < 0:
            return None
        area = math.sqrt(area_squared_triangle)
        return area
    except Exception:
        return None
if __name__ == '__main__':
    sample_sides_valid = [3, 4, 5]
    sample_sides_invalid_triangle = [1, 2, 10]
    sample_sides_too_few = [3, 4]
    sample_sides_non_positive = [3, 4, -5]
    sample_sides_odd_perimeter = [1, 1, 1]
    print(f"Sides {sample_sides_valid}: {calculate_heron_area(sample_sides_valid)}")
    print(f"Sides {sample_sides_invalid_triangle}: {calculate_heron_area(sample_sides_invalid_triangle)}")
    print(f"Sides {sample_sides_too_few}: {calculate_heron_area(sample_sides_too_few)}")
    print(f"Sides {sample_sides_non_positive}: {calculate_heron_area(sample_sides_non_positive)}")
    print(f"Sides {sample_sides_odd_perimeter}: {calculate_heron_area(sample_sides_odd_perimeter)}")