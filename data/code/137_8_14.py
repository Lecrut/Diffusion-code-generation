class LeapYearChecker:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2023]
    for year in sample_years:
        result = LeapYearChecker.is_leap_year(year)
        print(f"Year {year}: {'Leap Year' if result else 'Not a Leap Year'}")