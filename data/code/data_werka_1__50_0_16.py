def calculate_area_difference(area1, area2):
    if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
        raise ValueError("Both areas must be numbers.")
    return abs(area1 - area2)

if __name__ == '__main__':
    try:
        first_area = 100
        second_area = 60
        difference = calculate_area_difference(first_area, second_area)
        print(difference)
    except ValueError as e:
        print(e)