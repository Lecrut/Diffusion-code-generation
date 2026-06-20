HOUR_TO_SECONDS = 3600

def parse_time(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format")
    hours, minutes, seconds = map(int, parts)
    return hours * HOUR_TO_SECONDS + minutes * 60 + seconds

def calculate_elapsed_hours(start_time, end_time):
    try:
        start_seconds = parse_time(start_time)
        end_seconds = parse_time(end_time)
        elapsed_seconds = abs(end_seconds - start_seconds)
        return elapsed_seconds / HOUR_TO_SECONDS
    except ValueError as e:
        print(f"Error parsing time: {e}")
        return None

if __name__ == '__main__':
    sample_start_time = "12:30:00"
    sample_end_time = "15:45:00"
    result = calculate_elapsed_hours(sample_start_time, sample_end_time)
    print(f"Elapsed hours between {sample_start_time} and {sample_end_time}: {result}")