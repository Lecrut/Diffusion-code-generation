import datetime

def calculate_remaining_days(date):
    year = date.year
    month = date.month
    days_in_month = (datetime.date(year + (month == 12), month % 12 + 1, 1) - 
                     datetime.timedelta(days=1)).day
    today = datetime.date.today()
    if today < date:
        return days_in_month - (date.day - 1)
    else:
        return days_in_month - date.day

if __name__ == '__main__':
    current_date = datetime.date(2023, 10, 5)
    remaining_days = calculate_remaining_days(current_date)
    print(remaining_days)