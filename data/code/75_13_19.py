from datetime import datetime

def validate_timestamps(timestamp1: str, timestamp2: str) -> bool:
    try:
        datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
        datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def calculate_time_difference(timestamp1: str, timestamp2: str) -> tuple:
    date_format = '%Y-%m-%d %H:%M:%S'
    datetime1 = datetime.strptime(timestamp1, date_format)
    datetime2 = datetime.strptime(timestamp2, date_format)
    
    diff_seconds = abs((datetime2 - datetime1).total_seconds())
    hours = diff_seconds // 3600
    minutes = (diff_seconds % 3600) // 60
    seconds = diff_seconds % 60
    
    return int(hours), int(minutes), int(seconds)

if __name__ == '__main__':
    timestamp1 = "2023-01-15 12:30:45"
    timestamp2 = "2023-01-16 14:45:59"
    
    if validate_timestamps(timestamp1, timestamp2):
        hours, minutes, seconds = calculate_time_difference(timestamp1, timestamp2)
        print(f"Time difference between {timestamp1} and {timestamp2}: {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print("Invalid timestamps format. Please use 'YYYY-MM-DD HH:MM:SS'.")