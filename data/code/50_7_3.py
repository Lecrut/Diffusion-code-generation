def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_areas = {
        'area1': 75.3,
        'area2': 48.9
    }
    
    difference = calculate_area_difference(sample_areas['area1'], sample_areas['area2'])
    print(difference)