def calculate_duration(start_time, end_time):
    start_hour = int(start_time[:2])
    start_minute = int(start_time[3:])
    end_hour = int(end_time[:2])
    end_minute = int(end_time[3:])

    total_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    return total_minutes

if __name__ == '__main__':
    duration = calculate_duration('07:45', '18:23')
    print(duration)