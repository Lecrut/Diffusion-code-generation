def calculate_polygon_perimeter(sides):
    if not sides:
        return 0
    return sum(sides)

if __name__ == '__main__':
    polygon_sides = {
        'triangle': [3, 4, 5],
        'square': [10, 10, 10, 10],
        'pentagon': [6, 7, 8, 9, 10]
    }
    
    for name, sides in polygon_sides.items():
        perimeter = calculate_polygon_perimeter(sides)
        print(f"The perimeter of the {name} is: {perimeter}")