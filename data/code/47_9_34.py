class Triangle:
    BASE = 15
    HEIGHT = 7
    
    @staticmethod
    def calculate_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    print(Triangle.calculate_area(Triangle.BASE, Triangle.HEIGHT))