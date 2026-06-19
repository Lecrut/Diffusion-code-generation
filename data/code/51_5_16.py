def calculate_polygon_perimeter(sides):
    if not sides:
        return 0
    return sum(sides)

if __name__ == '__main__':
    polygons = {
        'triangle': [3, 4, 5],
        'square': [10, 10, 10, 10],
        'pentagon': [5, 5, 5, 5, 5]
    }
    
    for name, sides in polygons.items():
        perimeter = calculate_polygon_perimeter(sides)
        print(f"The perimeter of the {name} is: {perimeter}")