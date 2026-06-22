SIDE_A = 5
SIDE_B = 3

def calculate_area(side):
    return side * side

def sum_areas(area1, area2):
    return area1 + area2
if __name__ == '__main__':
    area_a = calculate_area(SIDE_A)
    area_b = calculate_area(SIDE_B)
    result = sum_areas(area_a, area_b)
    print(result)