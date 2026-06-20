class YearDifferenceCalculator:
    @staticmethod
    def calculate(year1: str, year2: str) -> int:
        return abs(int(year1) - int(year2))

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    difference = calculator.calculate('2023', '2019')
    print(f"The difference between 2023 and 2019 is: {difference}")