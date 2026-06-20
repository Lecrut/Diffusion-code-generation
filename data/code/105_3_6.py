from datetime import date

class DateHandler:
    def __init__(self, start_date):
        self.start_date = start_date

    def next_15th_day_of_month(self):
        current_year = self.start_date.year
        current_month = self.start_date.month + 1
        if current_month > 12:
            current_year += 1
            current_month = 1
        target_date = date(current_year, current_month, 1)
        while target_date.day < 15:
            target_date += timedelta(days=1)
        return target_date

if __name__ == '__main__':
    handler = DateHandler(date(2023, 3, 3))
    next_15th = handler.next_15th_day_of_month()
    print(next_15th)