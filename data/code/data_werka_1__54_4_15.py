import math

def validate_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    return True

def calculate_radius(diameter):
    return diameter / 2

def area_from_diameter(diameter):
    try:
        validate_diameter(diameter)
        radius = calculate_radius(diameter)
        area = math.pi * (radius ** 2)
        return area
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_diameters = [10, 5.5, -3, 'a']
    for diameter in sample_diameters:
        try:
            result = area_from_diameter(diameter)
            if result is not None:
                print(f"The area of a circle with diameter {diameter} is: {result}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")