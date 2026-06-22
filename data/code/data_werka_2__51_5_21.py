def calculate_polygon_perimeter(side_lengths):
    if not side_lengths:
        return 0
    total_length = sum(side_lengths)
    return total_length

if __name__ == '__main__':
    sample_side_lengths = [7, 8, 9]
    perimeter = calculate_polygon_perimeter(sample_side_lengths)
    print(perimeter)