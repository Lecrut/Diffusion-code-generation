def calculate_area_difference(area1, area2):
    areas = {
        'area1': area1,
        'area2': area2
    }
    return abs(areas['area1'] - areas['area2'])

if __name__ == '__main__':
    main_areas = {
        'first_area': 80,
        'second_area': 20
    }
    difference = calculate_area_difference(main_areas['first_area'], main_areas['second_area'])
    print(difference)