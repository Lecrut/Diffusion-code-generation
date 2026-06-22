from datetime import datetime
WEEKEND_DAYS = {5, 6}
HOLIDAY = '2023-10-12'

def is_weekend_or_holiday(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        weekday = date_obj.weekday()
        return weekday in WEEKEND_DAYS or date_str == HOLIDAY
    except ValueError:
        return False
if __name__ == '__main__':
    sample_date = '2023-10-12'
    result = is_weekend_or_holiday(sample_date)
    print(result)