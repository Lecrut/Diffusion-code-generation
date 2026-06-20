class YearRange:
    def __init__(self, start_year, end_year):
        if not isinstance(start_year, int) or not isinstance(end_year, int):
            raise ValueError("Both start_year and end_year must be integers.")
        if start_year > end_year:
            raise ValueError("start_year must be less than or equal to end_year.")
        
        self.start_year = start_year
        self.end_year = end_year

    def calculate_difference(self):
        return self.end_year - self.start_year

if __name__ == '__main__':
    year_range_instance = YearRange(2000, 2015)
    print(year_range_instance.calculate_difference())