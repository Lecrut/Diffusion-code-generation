from datetime import datetime

def time_difference(timestamp1, timestamp2):
    dt1 = datetime.fromisoformat(timestamp1)
    dt2 = datetime.fromisoformat(timestamp2)
    diff = dt2 - dt1
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    timestamp1 = '2023-04-01T12:00:00'
    timestamp2 = '2023-04-02T15:30:45'
    days, hours, minutes, seconds = time_difference(timestamp1, timestamp2)
    print(f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds')