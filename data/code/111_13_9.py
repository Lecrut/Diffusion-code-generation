import datetime

MONTHS_TO_ADD = 3

def add_months_to_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    future_month = (date_obj.month - 1 + MONTHS_TO_ADD) % 12 + 1
    future_year = date_obj.year + (date_obj.month - 1 + MONTHS_TO_ADD) // 12
    future_day = min(date_obj.day, datetime.date(future_year, future_month, 1).replace(day=1) - datetime.timedelta(days=1)).day
    return datetime.date(future_year, future_month, future_day)

if __name__ == '__main__':
    sample_date = "2023-12-20"
    result = add_months_to_date(sample_date)
    print(result)