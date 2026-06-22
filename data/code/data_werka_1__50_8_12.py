def compute_area_difference(area1, area2):
    return abs(area1 - area2)
UNITS = {'square meters': 'm²', 'square kilometers': 'km²', 'hectares': 'ha'}
if __name__ == '__main__':
    sample_areas = [(500, 200), (1500.5, 1200.5), (3.14, 2.85)]
    for area1, area2 in sample_areas:
        difference = compute_area_difference(area1, area2)
        print(f'The absolute difference between {area1} and {area2} is: {difference}')
    unit = UNITS['square meters']
    print(f'Difference in {unit}: {compute_area_difference(500, 200)} {unit}')