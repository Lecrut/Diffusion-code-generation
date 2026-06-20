import datetime

def calculate_minute_difference(date_string1, date_string2):
    format_string = '%Y-%m-%d %H:%M:%S'
    try:
        dt1 = datetime.datetime.strptime(date_string1, format_string)
        dt2 = datetime.datetime.strptime(date_string2, format_string)
        time_difference = abs(dt1 - dt2)
        total_minutes = time_difference.total_seconds() / 60
        return total_minutes
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

if __name__ == '__main__':
    sample_dates = {
        'date1': '2023-01-01 10:00:00',
        'date2': '2023-01-03 14:30:00'
    }
    
    try:
        result = calculate_minute_difference(sample_dates['date1'], sample_dates['date2'])
        print(result)
    except ValueError as e:
        print(e)