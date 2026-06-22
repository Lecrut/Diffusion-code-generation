from datetime import datetime

def time_difference(timestamp1, timestamp2):
    dt1 = datetime.fromtimestamp(timestamp1)
    dt2 = datetime.fromtimestamp(timestamp2)
    diff = abs(dt2 - dt1)
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)
if __name__ == '__main__':
    ts1 = 1672531200
    ts2 = 1672617600
    print(time_difference(ts1, ts2))