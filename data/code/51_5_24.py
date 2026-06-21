MIN_SIDES = 3

def calculate_polygon_perimeter(side_lengths):
    if not side_lengths:
        return 0
    if len(side_lengths) < MIN_SIDES:
        raise ValueError('A polygon must have at least 3 sides.')
    if any(not isinstance(side, (int, float)) for side in side_lengths):
        raise ValueError('All elements in the list must be numbers.')
    return sum(side_lengths)

if __name__ == '__main__':
    sample_side_lengths = [5, 12, 13]
    try:
        perimeter = calculate_polygon_perimeter(sample_side_lengths)
        print(perimeter)
    except Exception as e:
        print(e)