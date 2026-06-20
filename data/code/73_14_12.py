from datetime import datetime

def time_difference_in_hours(dt1, dt2):
    difference = dt2 - dt1
    hours = difference.total_seconds() / 3600.0
    return hours

if __name__ == '__main__':
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.strptime("2023-10-01 12:00:00", date_format)
    datetime2 = datetime.strptime("2023-10-01 14:30:00", date_format)
    result = time_difference_in_hours(datetime1, datetime2)
    print(result)