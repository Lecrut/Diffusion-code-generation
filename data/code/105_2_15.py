from datetime import datetime, timedelta

FRIDAY_INDEX = 4
REFERENCE_DATE = datetime(2023, 12, 15)

class DateCalculator:
    def __init__(self, base_date):
        if not isinstance(base_date, datetime):
            raise ValueError("base_date must be a datetime object")
        self.base_date = base_date

    def get_next_friday(self):
        current_weekday = self.base_date.weekday()
        days_to_add = FRIDAY_INDEX - current_weekday
        if days_to_add <= 0:
            days_to_add += 7
        return self.base_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    calc = DateCalculator(REFERENCE_DATE)
    next_friday = calc.get_next_friday()
    print(next_friday.strftime("%Y-%m-%d"))