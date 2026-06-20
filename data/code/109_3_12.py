from datetime import date

DAYS_IN_MONTH = 31

def days_left_in_month():
    today = date.today()
    _, last_day = date(today.year, today.month + 1, 1).timedelta(days=-1).isocalendar()
    return DAYS_IN_MONTH - today.day if last_day == 28 else last_day - today.day

if __name__ == '__main__':
    print(days_left_in_month())