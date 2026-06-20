from datetime import datetime

def calculate_time_difference():
    timestamp1 = datetime(2023, 10, 1, 12, 0, 0)
    timestamp2 = datetime(2023, 10, 1, 15, 30, 45)

    delta = timestamp2 - timestamp1
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(calculate_time_difference())