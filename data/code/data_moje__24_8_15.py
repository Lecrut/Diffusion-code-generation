LEAP_RULES = {
    'divisible_by_400': 400,
    'divisible_by_100': 100,
    'divisible_by_4': 4
}

def is_leap_year(year: int) -> bool:
    if year % LEAP_RULES['divisible_by_400'] == 0:
        return True
    if year % LEAP_RULES['divisible_by_100'] == 0:
        return False
    return year % LEAP_RULES['divisible_by_4'] == 0

class YearAnalyzer:
    def __init__(self, year: int):
        self.year = year

    def check_leap(self) -> bool:
        return is_leap_year(self.year)

if __name__ == '__main__':
    sample_years = [1600, 1700, 2400]
    for y in sample_years:
        analyzer = YearAnalyzer(y)
        result = analyzer.check_leap()
        print(f"Year {y} is a leap year: {result}")