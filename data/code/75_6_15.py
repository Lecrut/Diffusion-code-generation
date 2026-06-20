from datetime import datetime

def time_difference(date1, date2):
    delta = abs(date2 - date1)
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1, 12, 0, 0)
    date2 = datetime(2023, 10, 1, 14, 30, 45)
    hours, minutes, seconds = time_difference(date1, date2)
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")