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
    except Exception:
        return None
if __name__ == '__main__':
    sample1 = [3, 4, 5]
    sample2 = [5, 5, 5]
    sample3 = [1, 2, 10]
    sample4 = [1, 1, 1]
    sample5 = [1, 2]
    sample6 = [0, 4, 5]
    sample7 = [2, 3, 4, 5]
    print(f"Sides {sample1}: Area = {calculate_heron_area(sample1)}")
    print(f"Sides {sample2}: Area = {calculate_heron_area(sample2)}")
    print(f"Sides {sample3}: Area = {calculate_heron_area(sample3)}")
    print(f"Sides {sample4}: Area = {calculate_heron_area(sample4)}")
    print(f"Sides {sample5}: Area = {calculate_heron_area(sample5)}")
    print(f"Sides {sample6}: Area = {calculate_heron_area(sample6)}")
    print(f"Sides {sample7}: Area = {calculate_heron_area(sample7)}")