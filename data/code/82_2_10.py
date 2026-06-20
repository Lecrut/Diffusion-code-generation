class YearDifferenceCalculator:
    @staticmethod
    def calculate_difference(year1: str, year2: str) -> int:
        return abs(int(year1) - int(year2))

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    year_a = '2023'
    year_b = '1990'
    difference = calculator.calculate_difference(year_a, year_b)
    print(f"The difference between {year_a} and {year_b} is: {difference}")