from datetime import date, timedelta

def get_next_month_date(date_obj):
    next_month = date_obj.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = date(2023, 9, 15)
    print(get_next_month_date(sample_date))