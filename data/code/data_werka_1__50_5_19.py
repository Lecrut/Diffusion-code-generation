def area_difference(*areas):
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

if __name__ == '__main__':
    sample_areas = [10, 25, 15, 30]
    differences = list(area_difference(*sample_areas))
    print(differences)