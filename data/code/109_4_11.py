from datetime import datetime, timedelta

def remaining_hours_in_month(date_instance):
    current_year = date_instance.year
    current_month = date_instance.month
    next_month_first_day = datetime(current_year, current_month + 1, 1)
    last_day_of_current_month = next_month_first_day - timedelta(days=1)
    return (last_day_of_current_month - date_instance).days * 24
if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(remaining_hours_in_month(sample_date))