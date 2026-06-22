from datetime import date

class DaysRemainingCalculator:
    def days_left(self):
        today = date.today()
        last_day_of_month = self._get_last_day_of_current_month(today)
        return (last_day_of_month - today).days

    def _get_last_day_of_current_month(self, current_date):
        year = current_date.year
        month = current_date.month
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        try:
            last_day = date(year, month, 1) - timedelta(days=1)
        except ValueError:
            last_day = date(year + 1, 1, 1) - timedelta(days=1)
        return last_day

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())