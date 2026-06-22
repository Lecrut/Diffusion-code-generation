from datetime import date

def days_left_in_month():
    today = date.today()
    _, last_day_of_month = monthrange(today.year, today.month)
    last_day_of_current_month = date(today.year, today.month, last_day_of_month)
    return (last_day_of_current_month - today).days

if __name__ == '__main__':
    print(days_left_in_month())