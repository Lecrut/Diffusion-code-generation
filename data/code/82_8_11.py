class YearDifferenceCalculator:
    @staticmethod
    def calculate_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    sample_year_1 = 2023
    sample_year_2 = 1985
    difference = YearDifferenceCalculator.calculate_difference(sample_year_1, sample_year_2)
    print(difference)