import datetime

def get_day_of_month(year, month, day):
    try:
        date = datetime.date(year, month, day)
        return date.day
    except ValueError as e:
        print(f"Invalid date: {e}")
        return None

if __name__ == '__main__':
    sample_date = (2023, 10, 26)
    day_of_month = get_day_of_month(*sample_date)
    if day_of_month is not None:
        print(day_of_month)