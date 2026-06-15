def draw_box(coordinates):
    if not coordinates:
        return None
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    return (min_x, min_y, max_x, max_y)
if __name__ == '__main__':
    sample_coords = [
        (1, 5),
        (3, 5),
        (3, 7),
        (1, 7),
        (2, 6)
    ]
    box_bounds = draw_box(sample_coords)
    print(box_bounds)