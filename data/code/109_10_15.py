from datetime import date

def days_remaining_in_month():
    today = date.today()
    last_day_of_month = date(today.year, today.month, 28) + timedelta(days=4)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())