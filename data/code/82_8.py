class YearCalculator:
    @staticmethod
    def find_year_difference(year1, year2):
        return abs(year1 - year2)
if __name__ == '__main__':
    year_a = 2023
    year_b = 1998
    difference = YearCalculator.find_year_difference(year_a, year_b)
    print(difference)