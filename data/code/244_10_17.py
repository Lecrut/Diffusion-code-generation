def validate_circle_radius(radius):
    if radius <= 0:
        raise ValueError("Circle radius must be greater than zero")

def validate_rectangle_dimensions(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Rectangle dimensions must be greater than zero")

def circle_area(radius):
    validate_circle_radius(radius)
    return 3.14159 * radius ** 2

def rectangle_area(width, height):
    validate_rectangle_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    circle_radius = 5
    rectangle_width = 10
    rectangle_height = 7
    
    circle_area_result = circle_area(circle_radius)
    rectangle_area_result = rectangle_area(rectangle_width, rectangle_height)
    
    total_area = circle_area_result + rectangle_area_result
    print(total_area)