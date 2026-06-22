from datetime import datetime

def time_difference(timestamp1, timestamp2):
    dt1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    diff = dt2 - dt1
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds // 60) % 60
    seconds = diff.seconds % 60
    return f"{days}d {hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(time_difference("2023-10-01 12:00:00", "2023-10-05 14:30:45"))