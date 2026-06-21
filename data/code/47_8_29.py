class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_params = {'base': 9, 'height': 4}
    try:
        triangle = Triangle(triangle_params['base'], triangle_params['height'])
        print(f"The area of the triangle is: {triangle.area()}")
    except ValueError as e:
        print(e)