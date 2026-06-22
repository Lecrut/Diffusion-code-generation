import calendar

def days_left_in_month():
    today = datetime.date.today()
    year = today.year
    month = today.month
    _, num_days_in_month = calendar.monthrange(year, month)
    days_passed = (today - datetime.date(year, month, 1)).days + 1
    days_left = num_days_in_month - days_passed
    return days_left

if __name__ == '__main__':
    sample_result = days_left_in_month()
    print(sample_result)