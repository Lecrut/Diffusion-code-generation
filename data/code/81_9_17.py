TIME_FORMAT = "%H:%M:%S"
SECONDS_IN_HOUR = 3600

def parse_time(time_str):
    try:
        return tuple(int(part) for part in time_str.split(':'))
    except ValueError:
        raise ValueError("Invalid time format")

def time_to_seconds(time_tuple):
    hours, minutes, seconds = time_tuple
    return hours * SECONDS_IN_HOUR + minutes * 60 + seconds

def calculate_elapsed_hours(start_time, end_time):
    start_seconds = time_to_seconds(parse_time(start_time))
    end_seconds = time_to_seconds(parse_time(end_time))
    elapsed_seconds = abs(end_seconds - start_seconds)
    return elapsed_seconds / SECONDS_IN_HOUR

if __name__ == '__main__':
    sample_start_time = "09:15:30"
    sample_end_time = "17:45:15"
    result = calculate_elapsed_hours(sample_start_time, sample_end_time)
    print(f"Elapsed hours: {result}")