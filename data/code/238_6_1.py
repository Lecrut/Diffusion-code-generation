def draw_box(coordinates):
    if not coordinates:
        return None
    min_x = min(c[0] for c in coordinates)
    max_x = max(c[0] for c in coordinates)
    min_y = min(c[1] for c in coordinates)
    max_y = max(c[1] for c in coordinates)
    return (min_x, min_y, max_x, max_y)
if __name__ == '__main__':
    sample_coords = [
        (1, 5),
        (3, 2),
        (6, 8),
        (4, 7),
        (2, 6)
    ]
    box_boundaries = draw_box(sample_coords)
    print(box_boundaries)