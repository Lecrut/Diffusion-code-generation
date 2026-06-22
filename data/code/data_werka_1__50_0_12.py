def calculate_area_difference(area1, area2):
    if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
        raise ValueError("Both areas must be numerical values.")
    return abs(area1 - area2)

if __name__ == '__main__':
    try:
        area_a = 80
        area_b = 25
        difference = calculate_area_difference(area_a, area_b)
        print(difference)
    except ValueError as e:
        print(e)