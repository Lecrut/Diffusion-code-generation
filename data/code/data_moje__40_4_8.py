def calculate_rectangular_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    
    front_back_area = 2 * length * height
    left_right_area = 2 * width * height
    top_bottom_area = 2 * length * width
    
    total_surface_area = front_back_area + left_right_area + top_bottom_area
    return total_surface_area

if __name__ == '__main__':
    length = 10
    width = 5
    height = 7
    
    result = calculate_rectangular_surface_area(length, width, height)
    print(result)