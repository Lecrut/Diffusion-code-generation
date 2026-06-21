import math

def calculate_area_of_circle(radius: float) -> float:
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7.5
    try:
        area_result = calculate_area_of_circle(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {area_result}")
    except Exception as e:
        print(f"An error occurred: {e}")