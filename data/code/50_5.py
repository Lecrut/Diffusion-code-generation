def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return area1 - area2
    except ValueError:
        return "Error: Invalid input string"
if __name__ == '__main__':
    area_a = "10.5"
    area_b = "4.2"
    difference = calculate_area_difference(area_a, area_b)
    print(difference)
    area_c = "20"
    area_d = "5.5"
    difference2 = calculate_area_difference(area_c, area_d)
    print(difference2)
    area_e = "abc"
    area_f = "10"
    difference3 = calculate_area_difference(area_e, area_f)
    print(difference3)