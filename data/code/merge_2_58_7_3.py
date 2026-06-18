import datetime
def calculate_days_between(date1: datetime.date, date2: datetime.date) -> dict:
    delta = abs((date2 - date1).days)
    total_calendar_days = delta
    weekend_count = 0
    current_date = min(date1, date2) + datetime.timedelta(days=1) if date1 != date2 else max(date1, date2) - datetime.timedelta(days=1)
    while (current_date <= max(date1, date2)) or (current_date >= min(date1, date2)):
        is_weekend = current_date.weekday() >= 5
        if current_date.weekday() >= 5:
            weekend_count += 1
        current_date = datetime.timedelta(days=1) + current_date
    business_days = total_calendar_days - (weekend_count // 2 * 7)                                                                           
def calculate_business_and_calendar_days(date_a: datetime.date, date_b: datetime.date):
    start_date = min(date_a, date_b)
    end_date = max(date_a, date_b)
    total_span_days = (end_date - start_date).days
    current = start_date + datetime.timedelta(days=1)
    weekend_count = 0
    while current <= end_date:
        if current.weekday() >= 5:
            weekend_count += 1
        current += datetime.timedelta(days=1)
    total_days_inclusive = (end_date - start_date).days + 1
    current_check = start_date
    while current_check <= end_date:
        if current_check.weekday() >= 5:
            weekend_count += 1
        current_check += datetime.timedelta(days=1)
    business_days_inclusive = total_days_inclusive - weekend_count
    return {
        "calendar_days": (end_date - start_date).days,                                                                                                     
        "business_days": max(0, ((end_date - start_date).days + 1) - weekend_count) 
    }
def main():
    date_start = datetime.date(2023, 5, 1)
    date_end = datetime.date(2023, 6, 1)
    result = calculate_business_and_calendar_days(date_start, date_end)
    print(result)
if __name__ == '__main__':
    main()