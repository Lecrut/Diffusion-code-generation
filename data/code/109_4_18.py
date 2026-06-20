from datetime import datetime, timedelta

def remaining_hours_in_month(date_instance):
    current_date = date_instance.replace(day=1) + timedelta(days=31)
    last_day_of_month = current_date - timedelta(days=current_date.day)
    return (last_day_of_month - date_instance).days * 24

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_hours_in_month(sample_date))