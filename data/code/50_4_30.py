class AreaDifferenceCalculator:
    def __init__(self, *areas):
        self.areas = areas

    def calculate_differences(self):
        previous_area = None
        for area in self.areas:
            if previous_area is not None:
                yield abs(area - previous_area)
            previous_area = area

if __name__ == '__main__':
    sample_areas = [10, 25, 40, 35, 50]
    calculator = AreaDifferenceCalculator(*sample_areas)
    differences = list(calculator.calculate_differences())
    print(differences)