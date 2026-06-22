def area_of_rhombus(d1, d2):
    return 0.5 * d1 * d2

def sum_of_areas():
    area1 = area_of_rhombus(6, 8)
    area2 = area_of_rhombus(10, 12)
    return area1 + area2

if __name__ == '__main__':
    print(sum_of_areas())