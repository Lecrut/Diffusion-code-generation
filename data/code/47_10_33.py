class Triangle:
    BASE = 15
    HEIGHT = 4

    @staticmethod
    def calculate_area(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height

if __name__ == '__main__':
    try:
        area = Triangle.calculate_area(Triangle.BASE, Triangle.HEIGHT)
        print(area)
    except ValueError as e:
        print(e)