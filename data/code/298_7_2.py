from datetime import datetime

def time_difference(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = (end - start).seconds
    return duration

if __name__ == '__main__':
    print(time_difference('11:30', '14:15'))