class YearDifference:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year

    def calculate_difference(self):
        return abs(self.end_year - self.start_year)

if __name__ == '__main__':
    sample_start_year = 1980
    sample_end_year = 2023
    year_diff_instance = YearDifference(sample_start_year, sample_end_year)
    print(year_diff_instance.calculate_difference())