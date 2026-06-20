from datetime import datetime, timedelta

def remaining_hours_in_month(date_instance):
    year = date_instance.year
    month = date_instance.month
    last_day_of_month = (datetime(year, month + 1, 1) - timedelta(days=1)).day
    days_in_month = last_day_of_month - date_instance.day + 1
    remaining_hours = days_in_month * 24
    return remaining_hours

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(remaining_hours_in_month(sample_date))