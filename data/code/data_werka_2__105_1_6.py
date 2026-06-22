import datetime

class DateCalculator:
    BASE_YEAR = 2024
    BASE_MONTH = 1
    BASE_DAY = 1
    SUNDAY_INDEX = 6
    WEEK_DAYS = 7

    @staticmethod
    def calculate_first_sunday_after_start_date():
        base_date = datetime.date(DateCalculator.BASE_YEAR, DateCalculator.BASE_MONTH, DateCalculator.BASE_DAY)
        days_until_sunday = (DateCalculator.SUNDAY_INDEX - base_date.weekday()) % DateCalculator.WEEK_DAYS
        
        if days_until_sunday == 0:
            target_date = base_date + datetime.timedelta(days=DateCalculator.WEEK_DAYS)
        else:
            target_date = base_date + datetime.timedelta(days=days_until_sunday)
        
        return target_date

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_first_sunday_after_start_date()
    print(result)