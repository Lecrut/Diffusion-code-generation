import datetime

class DateHandler:
    def __init__(self):
        self.MONTHS = range(1, 13)

    @staticmethod
    def get_next_month(date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        year = date_obj.year
        month = date_obj.month
        
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        return datetime.date(next_year, next_month, date_obj.day)

if __name__ == '__main__':
    sample_date = "2023-12-15"
    handler = DateHandler()
    next_date = handler.get_next_month(sample_date)
    print(next_date.strftime("%Y-%m-%d"))