import datetime

def nearest_saturday(date_obj):
    days_until_saturday = (5 - date_obj.weekday()) % 7
    return date_obj + datetime.timedelta(days=days_until_saturday)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 1)
    next_saturday = nearest_saturday(sample_date)
    print(f"Nearest Saturday to {sample_date}: {next_saturday}")