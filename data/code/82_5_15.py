class YearDifference:
    def __init__(self, year1, year2):
        self.year1 = year1
        self.year2 = year2
    
    @staticmethod
    def calculate_difference(year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    year_diff_instance = YearDifference(2023, 1990)
    print(year_diff_instance.calculate_difference())