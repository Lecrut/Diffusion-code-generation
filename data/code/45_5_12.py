class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_circle_area(radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return GeometryUtils.PI * radius ** 2

if __name__ == '__main__':
    try:
        print(GeometryUtils.calculate_circle_area(5))
        print(GeometryUtils.calculate_circle_area(10.5))
        try:
            print(GeometryUtils.calculate_circle_area(-2))
        except ValueError as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")