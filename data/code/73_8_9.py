import datetime

def calculate_minute_difference(date_string1, date_string2):
    format_string = '%Y-%m-%d %H:%M:%S'
    try:
        dt1 = datetime.datetime.strptime(date_string1, format_string)
        dt2 = datetime.datetime.strptime(date_string2, format_string)
        time_difference = abs(dt1 - dt2)
        total_minutes = int(time_difference.total_seconds() / 60)
        return total_minutes
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

if __name__ == '__main__':
    try:
        date1 = '2023-01-01 10:00:00'
        date2 = '2023-01-01 11:30:45'
        result = calculate_minute_difference(date1, date2)
        print(result)
    except ValueError as e:
        print(e)