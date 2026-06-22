def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a numeric value")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric value")
    return width * height

if __name__ == '__main__':
    result = calculate_rectangle_area(5, 10)
    print(result)
    
    result_with_floats = calculate_rectangle_area(3.5, 2.0)
    print(result_with_floats)
    
    try:
        calculate_rectangle_area("5", 10)
    except TypeError as e:
        print(e)