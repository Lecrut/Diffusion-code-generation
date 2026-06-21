def validate_dates(dates):
    valid_formats = {'%Y-%m-%d'}
    for date in dates:
        if not any(date.strftime(format) == date for format in valid_formats):
            raise ValueError(f"Invalid date format: {date}")
    return True

def map_dates_to_days(dates):
    lookup = {
        '2023-04-01': 'Monday',
        '2023-04-02': 'Tuesday',
        '2023-04-03': 'Wednesday',
        '2023-04-04': 'Thursday',
        '2023-04-05': 'Friday'
    }
    return [lookup.get(date, 'Unknown') for date in dates]

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2023-04-06', '2023-04-03']
    validate_dates(sample_dates)
    print(map_dates_to_days(sample_dates))