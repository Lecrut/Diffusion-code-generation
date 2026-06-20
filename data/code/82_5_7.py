class YearRange:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
    
    def get_difference(self):
        return abs(self.end_year - self.start_year)

if __name__ == '__main__':
    year_range_instance = YearRange(1980, 2020)
    print(year_range_instance.get_difference())