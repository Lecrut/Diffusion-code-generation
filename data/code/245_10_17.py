import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    return length * width

def shapes_have_equal_areas(circle_radius, rectangle_length, rectangle_width):
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    epsilon = 1e-9
    if abs(circle_area - rectangle_area) < epsilon:
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        circle_radius = 5.0
        rectangle_length = 10.0
        rectangle_width = 5.0
        
        if shapes_have_equal_areas(circle_radius, rectangle_length, rectangle_width):
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except Exception as e:
        print(f"An error occurred: {e}")