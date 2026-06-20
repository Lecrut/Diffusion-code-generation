class YearDifferences:
    def __init__(self, years):
        self.years = years

    def differences(self):
        prev_year = None
        for year in self.years:
            if prev_year is not None:
                yield year - prev_year
            prev_year = year

if __name__ == '__main__':
    sample_years = [2000, 2010, 2020, 2030]
    calculator = YearDifferences(sample_years)
    for diff in calculator.differences():
        print(diff)