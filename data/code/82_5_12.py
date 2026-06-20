class YearDifferenceCalculator:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
    
    def calculate_difference(self):
        return abs(self.end_year - self.start_year)

if __name__ == '__main__':
    calculator_instance = YearDifferenceCalculator(2023, 1990)
    print(calculator_instance.calculate_difference())