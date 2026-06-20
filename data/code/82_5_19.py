class YearDifference:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
    
    def calculate_difference(self):
        return abs(self.end_year - self.start_year)

if __name__ == '__main__':
    year_diff_instance1 = YearDifference(2023, 1990)
    print(year_diff_instance1.calculate_difference())
    
    year_diff_instance2 = YearDifference(2000, 2015)
    print(year_diff_instance2.calculate_difference())