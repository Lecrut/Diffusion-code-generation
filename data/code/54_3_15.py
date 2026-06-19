import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        radius1 = 5.0
        area1 = calculate_circle_area(radius1)
        print(f"The area of a circle with radius {radius1} is: {area1}")
        
        radius2 = 2.5
        area2 = calculate_circle_area(radius2)
        print(f"The area of a circle with radius {radius2} is: {area2}")
        
        radius3 = -1.0
        area3 = calculate_circle_area(radius3)
        print(f"The area of a circle with radius {radius3} is: {area3}")
    except ValueError as e:
        print(e)