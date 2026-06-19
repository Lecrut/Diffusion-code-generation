class AreaCalculator:
    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    length = 9
    width = 6
    area = AreaCalculator.calculate_area(length, width)
    print(area)