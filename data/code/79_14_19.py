import datetime

def get_first_day_next_month(date_obj):
    year = date_obj.year + (date_obj.month == 12)
    month = 1 if date_obj.month == 12 else date_obj.month + 1
    return datetime.date(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2024, 3, 31)
    next_month_start = get_first_day_next_month(sample_date)
    print(next_month_start.strftime('%Y-%m-%d'))