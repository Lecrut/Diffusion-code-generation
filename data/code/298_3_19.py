from datetime import datetime, timedelta

def time_difference():
    start_time = datetime.strptime('23:59', '%H:%M')
    end_time = datetime.strptime('00:01', '%H:%M')
    if start_time > end_time:
        end_time += timedelta(days=1)
    return (end_time - start_time).total_seconds()

if __name__ == '__main__':
    print(time_difference())