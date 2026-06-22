class AreaDifferenceCalculator:

    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)
if __name__ == '__main__':
    area_a = 100
    area_b = 45
    calculator = AreaDifferenceCalculator(area_a, area_b)
    difference = calculator.calculate_difference()
    print('Difference between areas:', difference)
    area_c = 200
    area_d = 75
    calculator.update_areas(area_c, area_d)
    new_difference = calculator.calculate_difference()
    print('New difference between updated areas:', new_difference)

    class AreaDifferenceCalculator:

        def __init__(self, area1, area2):
            self.area1 = area1
            self.area2 = area2

        def calculate_difference(self):
            return abs(self.area1 - self.area2)

        def update_areas(self, new_area1, new_area2):
            self.area1 = new_area1
            self.area2 = new_area2
    if __name__ == '__main__':
        area_a = 100
        area_b = 45
        calculator = AreaDifferenceCalculator(area_a, area_b)
        difference = calculator.calculate_difference()
        print('Difference between areas:', difference)
        area_c = 200
        area_d = 75
        calculator.update_areas(area_c, area_d)
        new_difference = calculator.calculate_difference()
        print('New difference between updated areas:', new_difference)