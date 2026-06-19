PI = 3.141592653589793

def is_valid_radius(radius):
    return isinstance(radius, (int, float)) and radius >= 0

def calculate_circle_area(radius):
    if not is_valid_radius(radius):
        raise ValueError("Invalid radius: must be a non-negative number")
    return PI * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = 10.0
        area = calculate_circle_area(sample_radius)
        print(area)
    except ValueError as e:
        print(e)