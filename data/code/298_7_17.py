from datetime import datetime, timedelta

def time_difference(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = end - start
    return duration.total_seconds()

if __name__ == '__main__':
    print(time_difference('11:30', '14:15'))