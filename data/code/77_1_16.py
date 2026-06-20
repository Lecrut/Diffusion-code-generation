def time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_minutes = (hours * 60) + minutes + seconds / 60.0
    return total_minutes

if __name__ == '__main__':
    sample_time1 = "02:45:30"
    result1 = time_to_minutes(sample_time1)
    print(f"Time: {sample_time1}, Minutes: {result1}")
    
    sample_time2 = "12:00:00"
    result2 = time_to_minutes(sample_time2)
    print(f"Time: {sample_time2}, Minutes: {result2}")
    
    sample_time3 = "00:59:59"
    result3 = time_to_minutes(sample_time3)
    print(f"Time: {sample_time3}, Minutes: {result3}")