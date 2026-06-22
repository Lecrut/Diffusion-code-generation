from dateutil.relativedelta import relativedelta

def days_remaining(year, month):
    from datetime import date
    today = date.today()
    last_day_of_month = date(year, month + 1, 1) - relativedelta(days=1)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 5
    print(days_remaining(sample_year, sample_month))