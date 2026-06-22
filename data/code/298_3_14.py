from datetime import datetime

def time_difference():
    start_time = datetime.strptime('23:59', '%H:%M')
    end_time = datetime.strptime('00:01', '%H:%M')
    if start_time > end_time:
        end_time += timedelta(days=1)
    diff = (end_time - start_time).total_seconds() / 60
    return diff

if __name__ == '__main__':
    print(time_difference())