def calculate_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return area1 - area2
    except ValueError:
        return "Error: Invalid input string"
if __name__ == '__main__':
    area_a = "100.5"
    area_b = "45.2"
    result1 = calculate_difference(area_a, area_b)
    print(f"Difference between {area_a} and {area_b}: {result1}")
    area_c = "200"
    area_d = "150.75"
    result2 = calculate_difference(area_c, area_d)
    print(f"Difference between {area_c} and {area_d}: {result2}")
    area_e = "abc"
    area_f = "10"
    result3 = calculate_difference(area_e, area_f)
    print(f"Difference between {area_e} and {area_f}: {result3}")