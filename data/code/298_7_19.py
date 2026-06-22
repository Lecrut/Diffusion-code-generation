from datetime import datetime

def calculate_duration(start_time, end_time):
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = (end - start).seconds
    return duration

if __name__ == '__main__':
    total_duration = calculate_duration('11:30', '14:15')
    print(total_duration)