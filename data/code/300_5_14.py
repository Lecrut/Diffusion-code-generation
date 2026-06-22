import calendar

def days_left_in_month():
    today = datetime.date.today()
    month_range = calendar.monthrange(today.year, today.month)
    return month_range[1] - today.day + 1

if __name__ == '__main__':
    result = days_left_in_month()
    print(result)