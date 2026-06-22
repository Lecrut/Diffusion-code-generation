class AreaDifferenceCalculator:
    ERROR_MESSAGE = "Error: Invalid input string"

    @staticmethod
    def parse_area(area_str):
        try:
            return float(area_str)
        except ValueError:
            raise ValueError(AreaDifferenceCalculator.ERROR_MESSAGE)

    def __init__(self, *areas):
        self.areas = [AreaDifferenceCalculator.parse_area(area) for area in areas]

    def __iter__(self):
        for i in range(1, len(self.areas)):
            yield abs(self.areas[i] - self.areas[i - 1])

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator("10.5", "4.2", "20", "5.5")
    for diff in calculator:
        print(diff)