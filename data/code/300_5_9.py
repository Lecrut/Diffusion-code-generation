import calendar

def days_left_in_month():
    today = datetime.date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    return num_days - today.day

if __name__ == '__main__':
    result = days_left_in_month()
    print(result)