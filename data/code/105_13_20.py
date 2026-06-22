from datetime import date, timedelta

def find_next_weekend_date():
    today = date.today()
    weekday_index = today.weekday()
    if weekday_index == 5:
        target_date = today
    elif weekday_index == 6:
        target_date = today
    else:
        days_until_saturday = 5 - weekday_index
        target_date = today + timedelta(days=days_until_saturday)
    return target_date

if __name__ == '__main__':
    computed_date = find_next_weekend_date()
    print(computed_date)