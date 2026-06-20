from datetime import datetime

def time_difference(start_time: str, end_time: str) -> tuple:
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    delta = end - start
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    start_time = "2023-10-01 12:00:00"
    end_time = "2023-10-01 14:30:45"
    hours, minutes, seconds = time_difference(start_time, end_time)
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")