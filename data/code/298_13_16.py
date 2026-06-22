from datetime import datetime, timedelta

def validate_timestamp(timestamp):
    try:
        datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def calculate_time_difference(timestamp1, timestamp2):
    if not (validate_timestamp(timestamp1) and validate_timestamp(timestamp2)):
        raise ValueError("Invalid timestamp format provided.")
    
    time_format = '%Y-%m-%d %H:%M:%S'
    datetime1 = datetime.strptime(timestamp1, time_format)
    datetime2 = datetime.strptime(timestamp2, time_format)
    
    if datetime1 > datetime2:
        datetime1, datetime2 = datetime2, datetime1
    
    difference = datetime2 - datetime1
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds // 60) % 60
    seconds = difference.seconds % 60
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    timestamp_a = "2023-10-01 09:30:00"
    timestamp_b = "2023-10-01 14:45:30"
    days, hours, minutes, seconds = calculate_time_difference(timestamp_a, timestamp_b)
    print(f"{timestamp_a} to {timestamp_b}: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")