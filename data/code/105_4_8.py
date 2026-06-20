import datetime

def nearest_saturday(date_obj):
    delta = (5 - date_obj.weekday()) % 7
    return date_obj + datetime.timedelta(days=delta)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 1)
    next_saturday = nearest_saturday(sample_date)
    print(f"Nearest Saturday after {sample_date}: {next_saturday}")