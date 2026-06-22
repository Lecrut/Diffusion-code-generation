def time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute

def minutes_difference(time1_str, time2_str):
    time1_minutes = time_to_minutes(time1_str)
    time2_minutes = time_to_minutes(time2_str)
    if time1_minutes > time2_minutes:
        time2_minutes += 24 * 60
    return (time2_minutes - time1_minutes) // 60

if __name__ == '__main__':
    duration = minutes_difference('07:45', '18:23')
    print(duration)