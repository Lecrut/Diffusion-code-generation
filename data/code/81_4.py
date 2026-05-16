def time_difference_hours(time_str1, time_str2):
    time1 = time_str1.split(':')
    time2 = time_str2.split(':')
    h1 = int(time1[0])
    m1 = int(time1[1])
    s1 = int(time1[2])
    h2 = int(time2[0])
    m2 = int(time2[1])
    s2 = int(time2[2])
    total_seconds1 = h1 * 3600 + m1 * 60 + s1
    total_seconds2 = h2 * 3600 + m2 * 60 + s2
    difference_seconds = abs(total_seconds2 - total_seconds1)
    difference_hours = difference_seconds / 3600.0
    return difference_hours
if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)