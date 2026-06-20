from datetime import date, timedelta

def nearest_saturday(date_obj):
    days_to_saturday = (5 - date_obj.weekday()) % 7
    return date_obj + timedelta(days=days_to_saturday)

if __name__ == '__main__':
    sample_date = date(2023, 11, 1)
    next_saturday = nearest_saturday(sample_date)
    print(f"Sample Date: {sample_date}")
    print(f"Nearest Saturday: {next_saturday}")