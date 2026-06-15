class Geometry:
    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width
if __name__ == '__main__':
    length = 10
    width = 5
    area = Geometry.calculate_area_rectangle(length, width)
    print(area)