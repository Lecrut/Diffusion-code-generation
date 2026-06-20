from datetime import datetime

def time_difference():
    start_time = datetime(2023, 10, 1, 12, 0, 0)
    end_time = datetime(2023, 10, 1, 14, 30, 45)

    delta = end_time - start_time
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(time_difference())