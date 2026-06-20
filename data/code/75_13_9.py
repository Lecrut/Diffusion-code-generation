from datetime import datetime

def time_difference():
    start = datetime(2023, 4, 1, 12, 0, 0)
    end = datetime(2023, 4, 1, 15, 30, 45)
    delta = end - start
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(time_difference())