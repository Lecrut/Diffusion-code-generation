class YearDifferenceCalculator:
    @staticmethod
    def compute_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    sample_year1 = 2023
    sample_year2 = 1998
    result = YearDifferenceCalculator.compute_difference(sample_year1, sample_year2)
    print(result)