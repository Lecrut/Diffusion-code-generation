import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = {
        'small': 5,
        'medium': 10,
        'large': 15
    }
    
    for size, diameter in sample_diameters.items():
        try:
            area = calculate_circle_area(diameter)
            print(f"Area of {size} circle with diameter {diameter}: {area}")
        except ValueError as e:
            print(f"Error for {size} circle with diameter {diameter}: {e}")