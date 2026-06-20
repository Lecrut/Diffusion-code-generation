import datetime

def is_valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def calculate_next_occurrence(day_of_week, start_year, start_month, start_day):
    start_date = datetime.date(start_year, start_month, start_day)
    if not is_valid_date(start_year, start_month, start_day):
        raise ValueError('Invalid start date provided')
    days_ahead = (day_of_week - start_date.weekday()) % 7
    next_occurrence = start_date + datetime.timedelta(days=days_ahead)
    return next_occurrence
if __name__ == '__main__':
    sample_year, sample_month, sample_day = (2023, 9, 15)
    target_day_of_week = 3
    next_thursday = calculate_next_occurrence(target_day_of_week, sample_year, sample_month, sample_day)
    print(next_thursday.strftime('%Y-%m-%d'))