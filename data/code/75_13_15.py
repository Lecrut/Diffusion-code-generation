from datetime import datetime

def time_difference_human_readable(timestamp1, timestamp2):
    date_format = "%Y-%m-%d %H:%M:%S"
    start_time = datetime.strptime(timestamp1, date_format)
    end_time = datetime.strptime(timestamp2, date_format)
    
    delta = end_time - start_time
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60
    
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    start = "2023-10-01 09:00:00"
    end = "2023-10-01 14:30:45"
    result = time_difference_human_readable(start, end)
    print(result)