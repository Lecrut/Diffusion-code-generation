import calendar

def is_weekday(year, month, day):
    try:
        return calendar.weekday(year, month, day) < 5
    except ValueError as e:
        print(f"Invalid date: {e}")
        return False

if __name__ == '__main__':
    dates = [
        (2023, 10, 23),
        (2023, 10, 24),
        (2023, 10, 28),
        (2023, 10, 29)
    ]
    for date in dates:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {is_weekday(*date)}")