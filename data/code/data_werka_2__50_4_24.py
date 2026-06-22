def area_difference_generator(*areas):
    if not all(isinstance(area, (int, float)) and area >= 0 for area in areas):
        raise ValueError("All areas must be non-negative numbers.")
    
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

if __name__ == '__main__':
    sample_areas = [5, 15, 25, 35, 45]
    try:
        differences = list(area_difference_generator(*sample_areas))
        print(differences)
    except ValueError as e:
        print(e)