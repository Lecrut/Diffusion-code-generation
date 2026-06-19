def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_area1 = 50
    sample_area2 = 30
    result = calculate_area_difference(sample_area1, sample_area2)
    print(result)