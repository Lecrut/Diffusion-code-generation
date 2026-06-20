import datetime

class DateHandler:
    START_DATE = datetime.date(2023, 1, 15)
    
    @staticmethod
    def get_next_month_date(start_date):
        month_offset = (start_date.month % 12) + 1
        year = start_date.year + (month_offset // 12)
        next_month_day = min(start_date.day, [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month_offset - 1])
        return datetime.date(year, month_offset, next_month_day)
    
    @staticmethod
    def get_date_for_next_month():
        return DateHandler.get_next_month_date(DateHandler.START_DATE)

if __name__ == '__main__':
    next_month_date = DateHandler.get_date_for_next_month()
    print(next_month_date.strftime('%Y-%m-%d'))