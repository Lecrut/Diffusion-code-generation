class YearRange:

    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year

    def calculate_difference(self):
        if self.start_year > self.end_year:
            return None
        return self.end_year - self.start_year
if __name__ == '__main__':
    year_range_instance = YearRange(2015, 2000)
    difference = year_range_instance.calculate_difference()
    print(difference)