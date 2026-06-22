import math

class GeometryComparison:
    @staticmethod
    def calculate_sphere_surface_area(radius):
        return 4 * math.pi * radius ** 2
    
    @staticmethod
    def calculate_cube_surface_area(side_length):
        return 6 * side_length ** 2

if __name__ == '__main__':
    sphere_radius = 5.0
    cube_side_length = 5.0
    sphere_area = GeometryComparison.calculate_sphere_surface_area(sphere_radius)
    cube_area = GeometryComparison.calculate_cube_surface_area(cube_side_length)
    print(f"Sphere Surface Area: {sphere_area}")
    print(f"Cube Surface Area: {cube_area}")
    if math.isclose(sphere_area, cube_area):
        print("The areas are equal.")
    else:
        difference = abs(sphere_area - cube_area)
        print(f"The areas differ by: {difference}")