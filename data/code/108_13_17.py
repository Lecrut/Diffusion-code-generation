from datetime import date

def get_day_of_month(year=2024, month=10, day=10):
    try:
        return date(year, month, day).day
    except ValueError as e:
        print(f"Invalid date: {e}")
        return None

if __name__ == '__main__':
    day = get_day_of_month()
    if day is not None:
        print(day)