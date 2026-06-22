class Triangle:
    BASE = 10
    HEIGHT = 5

    @staticmethod
    def area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    print(Triangle.area(Triangle.BASE, Triangle.HEIGHT))