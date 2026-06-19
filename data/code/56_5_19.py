import math

def calculate_rectangle_diagonal(length, width):
    return math.sqrt(length**2 + width**2)

def calculate_circle_radius(diameter):
    return diameter / 2

if __name__ == '__main__':
    sample_values = {
        'rectangle_dimensions': (6, 8),
        'circle_diameter': 15
    }
    
    diagonal = calculate_rectangle_diagonal(*sample_values['rectangle_dimensions'])
    radius = calculate_circle_radius(sample_values['circle_diameter'])
    
    if radius != 0:
        ratio = diagonal / radius
        print(ratio)
    else:
        print("Undefined ratio (division by zero)")