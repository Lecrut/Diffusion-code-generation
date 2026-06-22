import math

def calculate_diagonal(length, width):
    return math.sqrt(length ** 2 + width ** 2)

def calculate_radius(area):
    return math.sqrt(area / math.pi)

if __name__ == '__main__':
    sample_values = {
        'rectangle_length': 6,
        'rectangle_width': 8,
        'circle_area': 50
    }
    
    diagonal = calculate_diagonal(sample_values['rectangle_length'], sample_values['rectangle_width'])
    radius = calculate_radius(sample_values['circle_area'])
    
    if radius != 0:
        ratio = diagonal / radius
        print(ratio)
    else:
        print("Undefined ratio (division by zero)")