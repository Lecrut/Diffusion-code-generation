from datetime import datetime

def time_difference(timestamp1, timestamp2):
    dt1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    diff = abs(dt2 - dt1)
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

if __name__ == '__main__':
    timestamp1 = "2023-10-01 12:00:00"
    timestamp2 = "2023-10-05 14:30:45"
    days, hours, minutes, seconds = time_difference(timestamp1, timestamp2)
    print(f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")