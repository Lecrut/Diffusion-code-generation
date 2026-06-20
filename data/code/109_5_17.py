import datetime

def calculate_remaining_minutes_in_month():
    today = datetime.date.today()
    last_day_of_month = today.replace(day=28) + datetime.timedelta(days=4)
    last_day_of_month = last_day_of_month - datetime.timedelta(days=last_day_of_month.day)
    remaining_days = (last_day_of_month - today).days
    remaining_minutes = remaining_days * 24 * 60
    return remaining_minutes

if __name__ == '__main__':
    sample_value = calculate_remaining_minutes_in_month()
    print(sample_value)