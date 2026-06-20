import datetime

def nearest_saturday(date_obj):
    days_ahead = (5 - date_obj.weekday()) % 7
    return date_obj + datetime.timedelta(days=days_ahead)

if __name__ == '__main__':
    target_date = datetime.date(2023, 11, 1)
    next_saturday = nearest_saturday(target_date)
    print(f"Nearest Saturday to {target_date}: {next_saturday}")