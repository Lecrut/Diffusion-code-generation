import math

SCALE_FACTORS = {
    "rectangle": 1.5,
    "circle": 2.0
}

RECTANGLE_WIDTH = 10
RECTANGLE_HEIGHT = 5

CIRCLE_RADIUS = 4

def scale_dimension(original_value, scale_factor):
    return original_value * scale_factor

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_scaled_rectangle_area(original_width, original_height, scale_factor):
    scaled_width = scale_dimension(original_width, scale_factor)
    scaled_height = scale_dimension(original_height, scale_factor)
    return calculate_rectangle_area(scaled_width, scaled_height)

def calculate_scaled_circle_area(original_radius, scale_factor):
    scaled_radius = scale_dimension(original_radius, scale_factor)
    return calculate_circle_area(scaled_radius)

if __name__ == '__main__':
    rect_area = calculate_scaled_rectangle_area(
        RECTANGLE_WIDTH,
        RECTANGLE_HEIGHT,
        SCALE_FACTORS["rectangle"]
    )
    print(rect_area)

    circle_area = calculate_scaled_circle_area(
        CIRCLE_RADIUS,
        SCALE_FACTORS["circle"]
    )
    print(circle_area)