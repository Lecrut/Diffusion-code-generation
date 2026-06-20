import datetime

def validate_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def get_day_of_week(year, month, day):
    if not validate_date(year, month, day):
        raise ValueError("Invalid date")
    date = datetime.date(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    print(f"Day of the week for {year}-{month:02d}-{day:02d}: {get_day_of_week(year, month, day)}")