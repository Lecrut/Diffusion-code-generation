class YearCalculator:
    @staticmethod
    def difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    print(YearCalculator.difference(2024, 2020))
    print(YearCalculator.difference(1990, 2000))
    print(YearCalculator.difference(2025, 2025))
    print(YearCalculator.difference(1800, 1750))