def calculate_polygon_perimeter(side_lengths):
    if not side_lengths:
        return 0
    return sum(side_lengths)

if __name__ == '__main__':
    sample_side_lengths = [3, 4, 5, 6]
    perimeter = calculate_polygon_perimeter(sample_side_lengths)
    print(perimeter)