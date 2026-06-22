import copy

def repeat_polygon(polygon, multiplier):
    return [copy.deepcopy(polygon) for _ in range(multiplier)]

if __name__ == '__main__':
    sample_polygon = {'vertices': [(0, 0), (1, 0), (1, 1)], 'color': 'green'}
    multiplier = 2
    repeated_polygons = repeat_polygon(sample_polygon, multiplier)
    print(repeated_polygons)