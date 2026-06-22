def calculate_polygon_perimeter(side_lengths):
    if not side_lengths:
        return 0
    
    perimeter = sum(side_lengths)
    return perimeter

if __name__ == '__main__':
    sample_sides = [3, 4, 5, 6]
    print(calculate_polygon_perimeter(sample_sides))