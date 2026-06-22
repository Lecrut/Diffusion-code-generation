def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be an integer or float.")
    return area

def find_area_difference(area1, area2):
    validated_area1 = validate_area(area1)
    validated_area2 = validate_area(area2)
    result = validated_area1 - validated_area2
    return abs(result)

if __name__ == '__main__':
    sample_areas = [
        (50, 25),
        (100, 35),
        (25.5, 15.0),
        (100, 100),
        (3.14159, 2.71828)
    ]
    
    for area1, area2 in sample_areas:
        difference = find_area_difference(area1, area2)
        print(f"The absolute difference between {area1} and {area2} is: {difference}")