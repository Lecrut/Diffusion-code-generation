class YearDifferenceGenerator:
    @staticmethod
    def year_differences(years):
        if len(years) < 2:
            raise ValueError("At least two years are required to calculate differences.")
        prev_year = years[0]
        for year in years[1:]:
            yield year - prev_year
            prev_year = year

if __name__ == '__main__':
    sample_years = [2000, 2005, 2010, 2015, 2020]
    generator = YearDifferenceGenerator()
    for diff in generator.year_differences(sample_years):
        print(diff)