def map_dates_to_days(dates):
    lookup = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    return [lookup.get(date, None) for date in dates]

if __name__ == '__main__':
    sample_dates = ['Monday', 'Wednesday', 'Friday']
    print(map_dates_to_days(sample_dates))