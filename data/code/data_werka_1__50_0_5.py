class AreaCalculator:
    @staticmethod
    def calculate_area_difference(area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 100
    area2 = 60
    difference = AreaCalculator.calculate_area_difference(area1, area2)
    print(difference)