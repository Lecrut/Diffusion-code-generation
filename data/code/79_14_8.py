import datetime

def validate_date(date_obj):
    if not isinstance(date_obj, datetime.datetime) or date_obj.year != 2024 or date_obj.month != 3 or date_obj.day != 31:
        raise ValueError("Invalid date. Expected: March 31, 2024")

def get_next_month_first_day():
    try:
        sample_date = datetime.datetime(2024, 3, 31)
        validate_date(sample_date)
        next_month = sample_date.replace(month=sample_date.month + 1, day=1)
        if next_month.month == 13:
            next_month = next_month.replace(year=next_month.year + 1, month=1)
        return next_month.strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    result = get_next_month_first_day()
    print(result)