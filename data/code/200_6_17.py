days_of_week = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday'
}

def map_dates_to_days(dates):
    return [days_of_week[date] for date in dates]

if __name__ == '__main__':
    sample_dates = ['1', '3', '5']
    print(map_dates_to_days(sample_dates))