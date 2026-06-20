class YearCalculator:
    def find_difference(self, year1: str, year2: str) -> int:
        return abs(int(year1) - int(year2))

if __name__ == '__main__':
    calculator = YearCalculator()
    year_a = '2023'
    year_b = '1990'
    difference = calculator.find_difference(year_a, year_b)
    print(f"The difference between {year_a} and {year_b} is: {difference}")