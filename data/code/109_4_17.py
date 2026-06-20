from datetime import datetime, timedelta

def remaining_hours_in_month(date_instance):
    current_date = date_instance.replace(day=1)
    next_month_first_day = current_date + timedelta(days=32)
    last_day_of_current_month = next_month_first_day - timedelta(days=1)
    return (last_day_of_current_month - date_instance).days * 24

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_hours_in_month(sample_date))