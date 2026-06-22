import calendar

def check_weekdays(dates):
    results = {}
    for date_str in dates:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        weekday = calendar.weekday(year, month, day)
        is_weekday = weekday < 5
        results[date_str] = is_weekday
    return results

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2023-10-02', '2023-10-07']
    print(check_weekdays(sample_dates))