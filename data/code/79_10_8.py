import datetime

def get_next_month_date(date):
    month_mapping = {12: (1, date.year + 1), default: (date.month + 1, date.year)}
    next_month, next_year = month_mapping.get(date.month, lambda x: (1, x))
    return datetime.date(next_year, next_month, 1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 4, 15)
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date)