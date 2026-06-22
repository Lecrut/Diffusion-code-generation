import math

def calculate_area(radius: float) -> float:
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = {
        'small': 0.5,
        'medium': 3.0,
        'large': 10.0
    }
    
    for size, radius in sample_radii.items():
        area = calculate_area(radius)
        print(f"The area of a circle with {size} radius ({radius}) is {area:.2f}")