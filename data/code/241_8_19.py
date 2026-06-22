def calculate_area(length: int, width: int) -> int:
    return length * width

if __name__ == '__main__':
    areas = {
        (5, 10): calculate_area(5, 10),
        (3, 4): calculate_area(3, 4),
        (7, 2): calculate_area(7, 2),
        (10, 10): calculate_area(10, 10)
    }
    
    for inputs, area in areas.items():
        print(f"Area of {inputs[0]} and {inputs[1]}: {area}")