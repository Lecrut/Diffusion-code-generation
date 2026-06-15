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
        (1, 2),
        (5, 2),
        (5, 6),
        (1, 6),
        (3, 4)
    ]
    box_boundaries = draw_box(sample_coords)
    print(box_boundaries)