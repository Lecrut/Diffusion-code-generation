def find_area_difference(area1, area2):
    result = area1 - area2
    return result
if __name__ == '__main__':
    area_a = 150
    area_b = 75
    difference = find_area_difference(area_a, area_b)
    print(f"The difference between {area_a} and {area_b} is: {difference}")