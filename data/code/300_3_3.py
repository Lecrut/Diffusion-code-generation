from datetime import datetime

def days_left_in_month():
    today = datetime.now()
    current_year, current_month = today.year, today.month
    _, last_day_of_current_month = calendar.monthrange(current_year, current_month)
    last_day = datetime(current_year, current_month, last_day_of_current_month)
    return (last_day - today).days

if __name__ == '__main__':
    result = days_left_in_month()
    print(result)