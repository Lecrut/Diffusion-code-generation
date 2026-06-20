import calendar

WEEKEND_DAYS = (5, 6)

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) not in WEEKEND_DAYS

if __name__ == '__main__':
    dates = [
        (2023, 10, 23),
        (2023, 10, 24),
        (2023, 10, 28),
        (2023, 10, 29)
    ]
    for date in dates:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {is_weekday(*date)}")