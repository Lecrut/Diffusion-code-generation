import datetime

def days_remaining_in_month():
    today = datetime.date.today()
    end_of_month = datetime.date(today.year, today.month, 1) + datetime.timedelta(days=32)
    return (end_of_month - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())