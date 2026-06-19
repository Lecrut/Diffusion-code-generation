def calculate_side_length(area):
    return area ** 0.5

if __name__ == '__main__':
    square_areas = {
        'square1': 25.0,
        'square2': 100.0,
        'square3': 49.0
    }
    
    for name, area in square_areas.items():
        side_length = calculate_side_length(area)
        print(f"The side length of {name} is: {side_length}")