import datetime

class DateHandler:
    def __init__(self, date_str):
        self.date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    def get_next_month_date(self):
        if self.date_obj.month == 12:
            next_month = self.date_obj.replace(year=self.date_obj.year + 1, month=1, day=1)
        else:
            next_month = self.date_obj.replace(month=self.date_obj.month + 1, day=self.date_obj.day)
        return next_month

if __name__ == '__main__':
    sample_date = "2023-10-15"
    handler = DateHandler(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"Next Month's Date: {handler.get_next_month_date()}")
    
    sample_date_dec = "2023-12-31"
    handler = DateHandler(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's Date: {handler.get_next_month_date()}")