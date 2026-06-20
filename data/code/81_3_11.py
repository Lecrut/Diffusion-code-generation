def parse_time(time_str: str) -> int:
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def calculate_elapsed_time(start_time_str: str, end_time_str: str) -> float:
    start_time = parse_time(start_time_str)
    end_time = parse_time(end_time_str)
    
    if end_time < start_time:
        end_time += 24 * 3600
    
    elapsed_seconds = end_time - start_time
    return elapsed_seconds / 3600.0

if __name__ == '__main__':
    start_time_str = "09:00:00"
    end_time_str = "17:30:00"
    elapsed = calculate_elapsed_time(start_time_str, end_time_str)
    print(f"{elapsed}")