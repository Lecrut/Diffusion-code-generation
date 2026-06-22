import copy

def repeat_polygon(polygon, multiplier):
    if not isinstance(polygon, dict) or 'vertices' not in polygon:
        raise ValueError("Invalid input: polygon must be a dictionary with 'vertices' key.")
    if not isinstance(multiplier, int) or multiplier < 0:
        raise ValueError("Invalid input: multiplier must be a non-negative integer.")
    
    return [copy.deepcopy(polygon) for _ in range(multiplier)]

if __name__ == '__main__':
    sample_polygon = {'vertices': [(0, 0), (1, 0), (1, 1)], 'color': 'red'}
    multiplier = 3
    repeated_polygons = repeat_polygon(sample_polygon, multiplier)
    print(repeated_polygons)