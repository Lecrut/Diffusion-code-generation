class YearDifferenceCalculator:
    def __init__(self, year1, year2):
        if not isinstance(year1, int) or not isinstance(year2, int):
            raise ValueError("Both inputs must be integers.")
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self):
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    calc_instance = YearDifferenceCalculator(2023, 1990)
    print(calc_instance.calculate_difference())