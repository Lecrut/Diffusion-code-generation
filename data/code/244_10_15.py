def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    circle_radius = 8
    rectangle_length = 10
    rectangle_width = 5
    
    circle_area_result = calculate_circle_area(circle_radius)
    rectangle_area_result = calculate_rectangle_area(rectangle_length, rectangle_width)
    
    total_area = circle_area_result + rectangle_area_result
    print(total_area)