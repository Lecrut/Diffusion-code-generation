from datetime import date, timedelta

def weekdays_left_in_month(reference_date=date(2023, 4, 1)):
    current_day = reference_date.day
    days_in_month = (reference_date.replace(day=28) + timedelta(days=4)).day
    remaining_days = days_in_month - current_day
    weekdays = sum(1 for _ in range(current_day, days_in_month + 1) if date(reference_date.year, reference_date.month, _).weekday() < 5)
    return weekdays

if __name__ == '__main__':
    print(weekdays_left_in_month())