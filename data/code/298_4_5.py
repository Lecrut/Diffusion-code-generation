def time_difference_minutes(time1_str, time2_str):
    time1_parts = list(map(int, time1_str.split(':')))
    time2_parts = list(map(int, time2_str.split(':')))
    
    if not (0 <= time1_parts[0] < 24 and 0 <= time1_parts[1] < 60 and
            0 <= time2_parts[0] < 24 and 0 <= time2_parts[1] < 60):
        raise ValueError("Invalid time format")
    
    total_minutes_time1 = time1_parts[0] * 60 + time1_parts[1]
    total_minutes_time2 = time2_parts[0] * 60 + time2_parts[1]
    
    if total_minutes_time1 > total_minutes_time2:
        total_minutes_time2 += 24 * 60
    
    return total_minutes_time2 - total_minutes_time1

if __name__ == '__main__':
    duration = time_difference_minutes('07:45', '18:23')
    print(f"Duration between 07:45 and 18:23 is {duration} minutes")