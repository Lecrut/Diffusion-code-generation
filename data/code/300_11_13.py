import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.date.today()
        first_day_of_next_month = self._get_first_day_of_next_month(today)
        return (first_day_of_next_month - today).days

    @staticmethod
    def _get_first_day_of_next_month(date_obj):
        if date_obj.month == 12:
            next_year = date_obj.year + 1
            next_month = 1
        else:
            next_year = date_obj.year
            next_month = date_obj.month + 1
        return datetime.date(next_year, next_month, 1)

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())