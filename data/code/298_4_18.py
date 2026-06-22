def parse_time(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute

def calculate_duration(start_time, end_time):
    start_minutes = parse_time(start_time)
    end_minutes = parse_time(end_time)
    
    if start_minutes > end_minutes:
        end_minutes += 24 * 60
    
    duration_minutes = end_minutes - start_minutes
    return duration_minutes

if __name__ == '__main__':
    time_a = "07:45"
    time_b = "18:23"
    result = calculate_duration(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {result} minutes")