import calendar

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    dates = [
        (2023, 11, 1),
        (2023, 11, 2),
        (2023, 11, 6),
        (2023, 11, 7)
    ]
    for date in dates:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {is_weekday(*date)}")