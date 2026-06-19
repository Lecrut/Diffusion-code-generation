def find_area_difference(area1, area2):
    try:
        result = abs(area1 - area2)
        return result
    except TypeError as e:
        raise ValueError("Both areas must be numbers.") from e

if __name__ == '__main__':
    sample_areas = [
        (50, 25),
        (100, 35),
        (25.5, 15.0),
        (100, 100),
        (3.14159, 2.71828)
    ]
    
    for area_a, area_b in sample_areas:
        difference = find_area_difference(area_a, area_b)
        print(f"The difference between {area_a} and {area_b} is: {difference}")