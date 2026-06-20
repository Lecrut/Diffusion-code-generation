import calendar

class DateValidator:
    YEAR = 2023
    MONTH = 10
    DAY = 15

    @staticmethod
    def get_day_of_month(year, month):
        return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    validator = DateValidator()
    day_of_month = validator.get_day_of_month(DateValidator.YEAR, DateValidator.MONTH)
    print(f"Day {DateValidator.DAY} of Month {DateValidator.MONTH} in the year {DateValidator.YEAR} falls on day number: {day_of_month}")