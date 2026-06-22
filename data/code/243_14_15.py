PI = 3.141592653589793

def calculate_circle_perimeter(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    return 2 * PI * radius

if __name__ == '__main__':
    sample_radius = 5
    perimeter = calculate_circle_perimeter(sample_radius)
    print(f"Perimeter of circle with radius {sample_radius}: {perimeter}")