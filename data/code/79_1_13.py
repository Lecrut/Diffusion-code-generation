from datetime import date, timedelta

def get_next_month_date(current_date):
    next_month = current_date.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = date(2023, 2, 15)
    print(get_next_month_date(sample_date))