DAYS_OF_WEEK = {
    '2023-04-01': 'Monday',
    '2023-04-02': 'Tuesday',
    '2023-04-03': 'Wednesday',
    '2023-04-04': 'Thursday',
    '2023-04-05': 'Friday'
}

def map_dates_to_days(dates):
    return [DAYS_OF_WEEK.get(date, 'Unknown') for date in dates]

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2023-04-06', '2023-04-03']
    print(map_dates_to_days(sample_dates))