import datetime

class DateHandler:
    @staticmethod
    def get_next_month(date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if date_obj.month == 12:
            next_month = date_obj.replace(year=date_obj.year + 1, month=1, day=1)
        else:
            next_month = date_obj.replace(month=date_obj.month + 1, day=1)
        return next_month

if __name__ == '__main__':
    handler = DateHandler()
    sample_date = "2023-10-15"
    next_date = handler.get_next_month(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"Next Month's Date: {next_date.strftime('%Y-%m-%d')}")
    
    sample_date_dec = "2023-12-31"
    next_date_dec = handler.get_next_month(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's Date: {next_date_dec.strftime('%Y-%m-%d')}")
    
    sample_date_jan = "2024-01-05"
    next_date_jan = handler.get_next_month(sample_date_jan)
    print(f"Original Date: {sample_date_jan}")
    print(f"Next Month's Date: {next_date_jan.strftime('%Y-%m-%d')}")