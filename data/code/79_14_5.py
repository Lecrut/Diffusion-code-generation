from datetime import datetime, timedelta

def get_first_day_next_month(date_obj):
    try:
        next_month = date_obj.replace(day=1) + timedelta(days=32)
        return next_month.replace(day=1).strftime('%Y-%m-%d')
    except Exception as e:
        return f'Error: {e}'
if __name__ == '__main__':
    sample_date = datetime(2024, 3, 31)
    result = get_first_day_next_month(sample_date)
    print(result)
    another_sample_date = datetime(2024, 5, 30)
    another_result = get_first_day_next_month(another_sample_date)
    print(another_result)