import math

class GeometryCalculator:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius**2
    
    @staticmethod
    def calculate_cube_surface_area(side):
        return 6 * side**2

if __name__ == '__main__':
    calculator = GeometryCalculator()
    circle_radius = 5.0
    cube_side = 5.0
    circle_area = calculator.calculate_circle_area(circle_radius)
    cube_surface_area = calculator.calculate_cube_surface_area(cube_side)
    print(f"Circle Area: {circle_area}")
    print(f"Cube Surface Area: {cube_surface_area}")
    if circle_area == cube_surface_area:
        print("The areas are equal.")
    else:
        difference = abs(circle_area - cube_surface_area)
        print(f"The areas differ by: {difference:.2f}")