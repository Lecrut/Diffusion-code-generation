def validate_areas(areas):
    for area in areas:
        if not isinstance(area, (int, float)) or area < 0:
            raise ValueError("All areas must be non-negative numbers.")

def area_difference_generator(*areas):
    validate_areas(areas)
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

if __name__ == '__main__':
    sample_areas = [10, 25, 35, 45, 55]
    try:
        differences = list(area_difference_generator(*sample_areas))
        print(differences)
    except ValueError as e:
        print(e)