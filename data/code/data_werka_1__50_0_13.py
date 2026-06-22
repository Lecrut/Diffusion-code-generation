class AreaCalculator:
    @staticmethod
    def calculate_area_difference(area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    area_first = 80
    area_second = 20
    difference = AreaCalculator.calculate_area_difference(area_first, area_second)
    print(difference)