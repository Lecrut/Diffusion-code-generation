import math

class Circle:
    PI = 3.141592653589793

    @staticmethod
    def calculate_area(diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be a positive number.")
        radius = diameter / 2
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    try:
        diameter1 = 10
        area1 = Circle.calculate_area(diameter1)
        print(f"The area of a circle with diameter {diameter1} is: {area1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        diameter2 = 0
        area2 = Circle.calculate_area(diameter2)
        print(f"The area of a circle with diameter {diameter2} is: {area2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        diameter3 = -5
        area3 = Circle.calculate_area(diameter3)
        print(f"The area of a circle with diameter {diameter3} is: {area3}")
    except ValueError as e:
        print(f"Error: {e}")