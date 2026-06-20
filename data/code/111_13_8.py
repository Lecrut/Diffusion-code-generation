import datetime

class DateAdder:
    MONTHS_TO_ADD = 1

    @staticmethod
    def add_months(date_obj):
        year = date_obj.year + (date_obj.month - 1) // 12
        month = ((date_obj.month - 1) % 12) + 1
        day = min(date_obj.day, [31, 29 if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime.date(year, month, day)

    @staticmethod
    def get_current_date():
        return datetime.date.today()

if __name__ == '__main__':
    current_date = DateAdder.get_current_date()
    future_date = DateAdder.add_months(current_date)
    print(future_date.strftime('%Y-%m-%d'))