import math

def compute_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 3.5
        area_result = compute_circle_area(sample_radius)
        print(area_result)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")