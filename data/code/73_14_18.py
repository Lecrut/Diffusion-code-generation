from datetime import datetime

def time_difference_in_hours(datetime1, datetime2):
    if not isinstance(datetime1, datetime) or not isinstance(datetime2, datetime):
        raise ValueError("Both inputs must be instances of datetime")
    
    difference = abs(datetime2 - datetime1)
    hours = difference.total_seconds() / 3600.0
    return hours

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 0, 0, 0)
    dt2 = datetime(2023, 1, 1, 4, 30, 0)
    result = time_difference_in_hours(dt1, dt2)
    print(result)