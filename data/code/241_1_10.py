class Geometry:
    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

if __name__ == '__main__':
    area = Geometry.calculate_rectangle_area(5, 3)
    print(area)