def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def absolute_time_difference(time1, time2):
    diff_minutes = time_to_minutes(time2) - time_to_minutes(time1)
    return diff_minutes if diff_minutes >= 0 else -diff_minutes

if __name__ == '__main__':
    time_a = '08:15'
    time_b = '20:45'
    difference = absolute_time_difference(time_a, time_b)
    print(difference)