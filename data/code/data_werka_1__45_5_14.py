class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_circle_area(radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return GeometryUtils.PI * radius * radius

if __name__ == '__main__':
    try:
        area1 = GeometryUtils.calculate_circle_area(5)
        print(f"Area for radius 5: {area1}")
        area2 = GeometryUtils.calculate_circle_area(10.5)
        print(f"Area for radius 10.5: {area2}")
        try:
            area3 = GeometryUtils.calculate_circle_area(-2)
        except ValueError as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")