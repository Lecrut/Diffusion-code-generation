from datetime import datetime

def calculate_time_difference():
    start_timestamp = "2023-10-01 12:00:00"
    end_timestamp = "2023-10-01 14:30:45"

    start_datetime = datetime.strptime(start_timestamp, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(end_timestamp, "%Y-%m-%d %H:%M:%S")

    time_difference = end_datetime - start_datetime

    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    seconds = time_difference.seconds % 60

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(calculate_time_difference())