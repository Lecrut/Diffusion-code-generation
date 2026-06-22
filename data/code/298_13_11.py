from datetime import datetime

def time_difference(timestamp1, timestamp2):
    dt1 = datetime.fromtimestamp(timestamp1)
    dt2 = datetime.fromtimestamp(timestamp2)
    diff = dt2 - dt1
    days = diff.days
    hours = diff.seconds // 3600
    minutes = diff.seconds % 3600 // 60
    seconds = diff.seconds % 60
    return (days, hours, minutes, seconds)
if __name__ == '__main__':
    timestamp1 = 1672531200
    timestamp2 = 1672617600
    days, hours, minutes, seconds = time_difference(timestamp1, timestamp2)
    print(f'Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds')