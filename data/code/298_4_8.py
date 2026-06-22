MINUTES_PER_HOUR = 60

def time_difference_minutes(time1_str, time2_str):
    hours1, minutes1 = map(int, time1_str.split(':'))
    hours2, minutes2 = map(int, time2_str.split(':'))
    
    total_minutes1 = hours1 * MINUTES_PER_HOUR + minutes1
    total_minutes2 = hours2 * MINUTES_PER_HOUR + minutes2
    
    if total_minutes1 > total_minutes2:
        total_minutes2 += MINUTES_PER_HOUR * 24
    
    return abs(total_minutes1 - total_minutes2)

if __name__ == '__main__':
    time_a = "07:45"
    time_b = "18:23"
    result = time_difference_minutes(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result} minutes")