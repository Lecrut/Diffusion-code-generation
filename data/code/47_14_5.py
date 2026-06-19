class Triangle:
    BASE_MULTIPLIER = 0.5

    @staticmethod
    def calculate_area(base: float, height: float) -> float:
        return Triangle.BASE_MULTIPLIER * base * height

if __name__ == '__main__':
    triangle_base = 20.0
    triangle_height = 10.0
    area = Triangle.calculate_area(triangle_base, triangle_height)
    print(area)