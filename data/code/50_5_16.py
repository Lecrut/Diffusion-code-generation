class AreaDifferenceCalculator:

    @staticmethod
    def parse_area(area_str):
        try:
            return float(area_str)
        except ValueError:
            raise ValueError(f'Invalid input string: {area_str}')

    def __init__(self, *areas):
        self.areas = [AreaDifferenceCalculator.parse_area(area) for area in areas]

    def calculate_differences(self):
        previous_area = None
        for area in self.areas:
            if previous_area is not None:
                yield abs(previous_area - area)
            previous_area = area
if __name__ == '__main__':
    calculator = AreaDifferenceCalculator('10.5', '4.2', '20', '5.5')
    differences = list(calculator.calculate_differences())
    print(differences)