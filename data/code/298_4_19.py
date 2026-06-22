def time_difference_minutes(time1_str, time2_str):
    time_format = "%H:%M"
    time1 = datetime.datetime.strptime(time1_str, time_format)
    time2 = datetime.datetime.strptime(time2_str, time_format)
    
    if time1 > time2:
        time2 += datetime.timedelta(days=1)
    
    difference = time2 - time1
    total_minutes = difference.total_seconds() / 60
    
    return int(total_minutes)

if __name__ == '__main__':
    time_a = "07:45"
    time_b = "18:23"
    result = time_difference_minutes(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result} minutes")