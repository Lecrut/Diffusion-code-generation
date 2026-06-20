import calendar

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 5),
        (2023, 10, 6),
        (2023, 10, 10),
        (2023, 10, 11)
    ]
    for date in sample_dates:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {is_weekday(*date)}")