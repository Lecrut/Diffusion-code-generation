def calculate_square_area(side_length):
    return side_length ** 2

def sum_areas(side1, side2):
    area1 = calculate_square_area(side1)
    area2 = calculate_square_area(side2)
    return area1 + area2

if __name__ == '__main__':
    s1 = 6
    s2 = 8
    result = sum_areas(s1, s2)
    print(result)