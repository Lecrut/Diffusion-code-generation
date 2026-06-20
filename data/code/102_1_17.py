import calendar

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 2),
        (2023, 10, 3),
        (2023, 10, 7),
        (2023, 10, 8)
    ]
    
    for date in sample_dates:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {is_weekday(*date)}")