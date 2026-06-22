from datetime import date, timedelta

class DateCalculator:
    WEDNESDAY_INDEX = 2
    DAYS_IN_WEEK = 7

    @staticmethod
    def find_next_wednesday(target_date: date) -> date:
        current_weekday = target_date.weekday()
        days_until_wednesday = DateCalculator.WEDNESDAY_INDEX - current_weekday
        if days_until_wednesday <= 0:
            days_until_wednesday += DateCalculator.DAYS_IN_WEEK
        return target_date + timedelta(days=days_until_wednesday)

if __name__ == '__main__':
    start_date = date(2023, 10, 10)
    calculator = DateCalculator()
    result = calculator.find_next_wednesday(start_date)
    print(result)