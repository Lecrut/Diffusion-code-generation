def calculate_perimeter(side_lengths):
    return sum(side_lengths)

if __name__ == '__main__':
    polygon_sides = [7, 5, 3, 4, 2]
    perimeter = calculate_perimeter(polygon_sides)
    print(perimeter)