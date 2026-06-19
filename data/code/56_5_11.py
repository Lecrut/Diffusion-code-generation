import math

def calculate_rectangle_diagonal(length, width):
    return math.sqrt(length**2 + width**2)

def calculate_circle_radius(diameter):
    return diameter / 2

if __name__ == '__main__':
    dimensions = {
        'rectangle': {'length': 6, 'width': 8},
        'circle': {'diameter': 10}
    }
    
    rectangle_diagonal = calculate_rectangle_diagonal(
        dimensions['rectangle']['length'], 
        dimensions['rectangle']['width']
    )
    circle_radius = calculate_circle_radius(dimensions['circle']['diameter'])
    
    if circle_radius != 0:
        ratio = rectangle_diagonal / circle_radius
        print(ratio)
    else:
        print("Undefined ratio (division by zero)")