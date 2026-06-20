import datetime

def get_day_of_week(year, month, day):
    try:
        date = datetime.date(year, month, day)
        return date.strftime('%A')
    except ValueError:
        raise ValueError("Invalid date. Please provide a valid year, month, and day.")

if __name__ == '__main__':
    print(get_day_of_week(2024, 2, 29))