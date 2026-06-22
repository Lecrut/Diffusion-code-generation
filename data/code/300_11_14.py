import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.date.today()
        first_day_of_next_month = datetime.date(today.year, today.month + 1, 1)
        if first_day_of_next_month.month == 1:
            first_day_of_next_month = first_day_of_next_month.replace(year=today.year + 1)
        days_in_current_month = (first_day_of_next_month - datetime.timedelta(days=1)).day
        return days_in_current_month - today.day

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())