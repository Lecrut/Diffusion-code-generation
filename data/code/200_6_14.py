def map_dates_to_days(dates):
    day_names = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return [day_names[date.weekday()] for date in dates]

if __name__ == '__main__':
    from datetime import date
    sample_dates = [
        date(2023, 1, 1),
        date(2023, 1, 2),
        date(2023, 1, 3),
        date(2023, 1, 4),
        date(2023, 1, 5)
    ]
    print(map_dates_to_days(sample_dates))