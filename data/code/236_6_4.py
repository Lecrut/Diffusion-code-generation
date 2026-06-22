def repeat_polygon(polygon, multiplier):
    return [polygon] * multiplier

if __name__ == '__main__':
    sample_polygon = {'vertices': [(0, 0), (1, 0), (1, 1), (0, 1)]}
    multiplier = 3
    repeated_polygons = repeat_polygon(sample_polygon, multiplier)
    print(repeated_polygons)