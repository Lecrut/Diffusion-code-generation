import copy

def repeat_polygon(polygon, multiplier):
    return [copy.deepcopy(polygon) for _ in range(multiplier)]

if __name__ == '__main__':
    SAMPLE_POLYGON = {'vertices': [(0, 0), (1, 0), (1, 1)], 'color': 'green'}
    MULTIPLIER = 3
    REPEATED_POLYGONS = repeat_polygon(SAMPLE_POLYGON, MULTIPLIER)
    print(REPEATED_POLYGONS)