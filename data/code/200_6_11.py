def map_dates_to_days(dates):
    lookup = {
        '2023-04-01': 'Monday',
        '2023-04-02': 'Tuesday',
        '2023-04-03': 'Wednesday',
        '2023-04-04': 'Thursday',
        '2023-04-05': 'Friday'
    }
    
    if not all(isinstance(date, str) for date in dates):
        raise ValueError("All items in the input list must be strings.")
    
    return [lookup.get(date, 'Unknown') for date in dates]

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2023-04-06', '2023-04-03']
    print(map_dates_to_days(sample_dates))