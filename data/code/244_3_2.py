def calculate_sum_of_square_areas(side1, side2):
    area1 = side1 * side1
    area2 = side2 * side2
    return area1 + area2
if __name__ == '__main__':
    s1 = 3.5
    s2 = 4.2
    result = calculate_sum_of_square_areas(s1, s2)
    print(result)