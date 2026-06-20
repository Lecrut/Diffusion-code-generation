from datetime import datetime

def calculate_time_difference(timestamp1, timestamp2):
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        time1 = datetime.strptime(timestamp1, date_format)
        time2 = datetime.strptime(timestamp2, date_format)
        diff = abs(time2 - time1)
        
        hours = diff.seconds // 3600
        minutes = (diff.seconds // 60) % 60
        seconds = diff.seconds % 60
        
        return f"{hours} hours {minutes} minutes {seconds} seconds"
    except ValueError:
        return "Invalid timestamp format. Please use 'YYYY-MM-DD HH:MM:SS'."

if __name__ == '__main__':
    timestamp1 = "2023-01-15 14:30:00"
    timestamp2 = "2024-03-20 18:45:30"
    result = calculate_time_difference(timestamp1, timestamp2)
    print(result)