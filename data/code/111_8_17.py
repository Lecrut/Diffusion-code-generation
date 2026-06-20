from datetime import date

class DateRangeCalculator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def count_weekdays(self):
        weekdays = 0
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date.weekday() < 5:
                weekdays += 1
            current_date += timedelta(days=1)
        return weekdays

if __name__ == '__main__':
    calculator = DateRangeCalculator(date(2023, 6, 1), date(2023, 8, 31))
    print(calculator.count_weekdays())