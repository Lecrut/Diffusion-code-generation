import datetime

def weekdays_left_in_month(reference_date):
    today = reference_date
    _, num_days = calendar.monthrange(today.year, today.month)
    weekday_count = 0
    for day in range(1, num_days + 1):
        if (today.replace(day=day)).weekday() < 5:
            weekday_count += 1
    return weekday_count

if __name__ == '__main__':
    reference_date = datetime.date(2023, 4, 1)
    print(weekdays_left_in_month(reference_date))