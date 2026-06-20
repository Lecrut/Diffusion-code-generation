class LeapYearCalculator:
    LEAP_YEAR_MASK = 0b100
    NOT_LEAP_YEAR_MASK = 0b011

    @staticmethod
    def is_leap_year(year):
        return (year & LeapYearCalculator.LEAP_YEAR_MASK == 0) and \
               ((year & LeapYearCalculator.NOT_LEAP_YEAR_MASK != 0) or (year % 400 == 0))

    @classmethod
    def count_leap_years(cls, start_year, end_year):
        count = 0
        for year in range(start_year, end_year + 1):
            if cls.is_leap_year(year):
                count += 1
        return count

if __name__ == '__main__':
    calculator = LeapYearCalculator()
    print(calculator.count_leap_years(2000, 2023))