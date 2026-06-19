class Triangle:
    BASE = 10.0
    HEIGHT = 5.0

    @staticmethod
    def calculate_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    area = Triangle.calculate_area(Triangle.BASE, Triangle.HEIGHT)
    print(area)