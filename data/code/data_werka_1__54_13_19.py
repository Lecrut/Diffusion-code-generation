import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def calculate_area(radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    try:
        area = Circle.calculate_area(sample_radius)
        print(area)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")