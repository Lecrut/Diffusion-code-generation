from datetime import date

def days_left_in_month():
    today = date.today()
    year, month = today.year, today.month
    _, last_day_of_month = date(year, month + 1, 1).isocalendar()[:2]
    return (date(year, month, last_day_of_month) - today).days

if __name__ == '__main__':
    result = days_left_in_month()
    print(result)