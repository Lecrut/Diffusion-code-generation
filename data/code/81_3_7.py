HOURS_TO_SECONDS = 3600

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * HOURS_TO_SECONDS + minutes * 60 + seconds

def calculate_elapsed_time(start_time_str, end_time_str):
    start_seconds = time_to_seconds(start_time_str)
    end_seconds = time_to_seconds(end_time_str)
    elapsed_seconds = abs(end_seconds - start_seconds)
    elapsed_hours = elapsed_seconds / HOURS_TO_SECONDS
    return elapsed_hours

if __name__ == '__main__':
    start_time_str = "09:00:00"
    end_time_str = "17:30:00"
    elapsed = calculate_elapsed_time(start_time_str, end_time_str)
    print(f"{elapsed}")