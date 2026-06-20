class YearDifferences:
    def __init__(self, years):
        self.years = years

    @staticmethod
    def calculate_differences(years):
        prev_year = None
        for year in years:
            if prev_year is not None:
                yield year - prev_year
            prev_year = year

if __name__ == '__main__':
    sample_years = [1990, 2000, 2010, 2020]
    differences = YearDifferences(sample_years)
    for diff in differences.calculate_differences(differences.years):
        print(diff)