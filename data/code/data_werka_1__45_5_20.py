class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_circle_area(radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return GeometryUtils.PI * radius ** 2

if __name__ == '__main__':
    try:
        radius1 = 7
        area1 = GeometryUtils.calculate_circle_area(radius1)
        print(f"Area for radius {radius1}: {area1}")

        radius2 = 3.5
        area2 = GeometryUtils.calculate_circle_area(radius2)
        print(f"Area for radius {radius2}: {area2}")
    except ValueError as e:
        print(f"Error: {e}")