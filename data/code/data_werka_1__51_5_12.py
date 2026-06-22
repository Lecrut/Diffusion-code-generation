def calculate_polygon_perimeter(side_lengths):
    if not side_lengths:
        return 0
    return sum(side_lengths)

if __name__ == '__main__':
    polygon_sides = {
        'triangle': [3, 4, 5],
        'square': [4, 4, 4, 4],
        'pentagon': [5, 5, 5, 5, 5]
    }
    
    for name, sides in polygon_sides.items():
        perimeter = calculate_polygon_perimeter(sides)
        print(f"The perimeter of the {name} is: {perimeter}")