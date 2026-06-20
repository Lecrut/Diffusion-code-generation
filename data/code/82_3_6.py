class YearDifferences:
    @staticmethod
    def calculate_differences(years):
        prev_year = None
        for year in years:
            if prev_year is not None:
                yield year - prev_year
            prev_year = year

if __name__ == '__main__':
    sample_years = [2000, 2015, 2030, 2045]
    differences = YearDifferences.calculate_differences(sample_years)
    for diff in differences:
        print(diff)