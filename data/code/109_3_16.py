from datetime import date

DAYS_IN_MONTH = 31

def days_left_in_month():
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    return num_days - today.day + 1

if __name__ == '__main__':
    print(days_left_in_month())