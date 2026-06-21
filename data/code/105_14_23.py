import datetime

class DateCalculator:
    MONDAY_INDEX = 0
    DAYS_IN_WEEK = 7

    @staticmethod
    def get_next_monday():
        today = datetime.date.today()
        current_weekday = today.weekday()
        days_until_monday = (DateCalculator.MONDAY_INDEX - current_weekday) % DateCalculator.DAYS_IN_WEEK
        if days_until_monday == 0:
            days_until_monday = DateCalculator.DAYS_IN_WEEK
        next_monday = today + datetime.timedelta(days=days_until_monday)
        return next_monday

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.get_next_monday()
    print(result)