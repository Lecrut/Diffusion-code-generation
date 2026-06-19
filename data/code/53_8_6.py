def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    sample_areas = {
        'tiny': 4,
        'small': 16,
        'medium': 36,
        'large': 64
    }
    for description, area in sample_areas.items():
        try:
            side_length = find_side_length(area)
            print(f"The side length of the {description} square with area {area} is: {side_length}")
        except ValueError as e:
            print(e)