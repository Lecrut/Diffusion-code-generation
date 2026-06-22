import datetime

def calculate_remaining_days(date_obj):
    last_day_of_month = datetime.date(date_obj.year, date_obj.month, 1) + datetime.timedelta(days=32)
    first_day_of_next_month = last_day_of_month.replace(day=1)
    return (first_day_of_next_month - date_obj).days

if __name__ == '__main__':
    current_date = datetime.date(2023, 10, 5)
    remaining_days = calculate_remaining_days(current_date)
    print(remaining_days)