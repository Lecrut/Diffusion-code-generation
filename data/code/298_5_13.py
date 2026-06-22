import datetime

def time_difference(time1_str, time2_str):
    time_format = '%H:%M'
    time1 = datetime.datetime.strptime(time1_str, time_format)
    time2 = datetime.datetime.strptime(time2_str, time_format)
    if time2 > time1:
        diff = time2 - time1
        return int(diff.total_seconds() / 3600)
    else:
        raise ValueError('Second time is not chronologically after the first time')
if __name__ == '__main__':
    time_a = '12:00'
    time_b = '19:30'
    try:
        result = time_difference(time_a, time_b)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')