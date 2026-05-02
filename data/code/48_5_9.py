import math
def calculate_heron_area(side_lengths):
    if len(side_lengths) < 3:
        return None
    s = sum(side_lengths)
    if s % 2 != 0:
        return None
    s_half = s / 2
    if any(length <= 0 for length in side_lengths):
        return None
    try:
        area_squared = s_half * (s_half - side_lengths[0]) * (s_half - side_lengths[1]) * (s_half - side_lengths[2])
        if len(side_lengths) == 3:
            area = math.sqrt(s_half * (s_half - side_lengths[0]) * (s_half - side_lengths[1]) * (s_half - side_lengths[2]))
            return area
        else:
            return None
    except ValueError:
        return None
if __name__ == '__main__':
    sample_sides_valid = [3, 4, 5]
    sample_sides_invalid_triangle = [1, 2, 10]
    sample_sides_too_few = [3, 4]
    sample_sides_non_positive = [3, 4, -5]
    sample_sides_odd_perimeter = [2, 3, 4]
    print(f"Sides {sample_sides_valid}: Area = {calculate_heron_area(sample_sides_valid)}")
    print(f"Sides {sample_sides_invalid_triangle}: Area = {calculate_heron_area(sample_sides_invalid_triangle)}")
    print(f"Sides {sample_sides_too_few}: Area = {calculate_heron_area(sample_sides_too_few)}")
    print(f"Sides {sample_sides_non_positive}: Area = {calculate_heron_area(sample_sides_non_positive)}")
    print(f"Sides {sample_sides_odd_perimeter}: Area = {calculate_heron_area(sample_sides_odd_perimeter)}")