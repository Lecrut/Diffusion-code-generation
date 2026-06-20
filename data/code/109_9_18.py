import datetime

def days_until_end_of_month(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    end_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    today = datetime.date.today()
    remaining_days = (end_of_month - today).days
    return remaining_days

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    days_left = days_until_end_of_month(sample_year, sample_month)
    print(days_left)