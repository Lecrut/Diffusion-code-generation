from datetime import datetime

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def absolute_time_difference(time1, time2):
    t1 = time_to_minutes(time1)
    t2 = time_to_minutes(time2)
    diff = abs(t2 - t1)
    if t2 < t1:
        diff = -diff
    return diff

if __name__ == '__main__':
    sample_time_a = '08:15'
    sample_time_b = '20:45'
    difference = absolute_time_difference(sample_time_a, sample_time_b)
    print(difference)