from datetime import datetime

def time_difference(date1, date2):
    delta = abs(date2 - date1)
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1, 12, 0, 0)
    date2 = datetime(2023, 10, 1, 14, 30, 45)
    print(time_difference(date1, date2))