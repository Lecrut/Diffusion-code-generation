def calculate_area_difference(area1, area2):
    difference = abs(area1 - area2)
    return difference
if __name__ == '__main__':
    a = 15.5
    b = 8.2
    result = calculate_area_difference(a, b)
    print(result)