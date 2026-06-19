import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    circle_sizes = {
        'tiny': 0.5,
        'small': 1,
        'medium': 5,
        'large': 10,
        'huge': 20
    }
    
    for size, radius in circle_sizes.items():
        area = calculate_circle_area(radius)
        print(f"The area of a {size} circle with radius {radius} is: {area}")