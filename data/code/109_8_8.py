from datetime import date, timedelta

def weekdays_left_in_month(reference_date=date(2023, 4, 1)):
    today = reference_date
    end_of_month = date(today.year, today.month + 1, 1) - timedelta(days=1)
    weekday_count = 0
    while today <= end_of_month:
        if today.weekday() < 5:
            weekday_count += 1
        today += timedelta(days=1)
    return weekday_count
if __name__ == '__main__':
    print(weekdays_left_in_month())