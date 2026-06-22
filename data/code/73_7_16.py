from datetime import datetime

FORMAT_PATTERN = '%Y-%m-%d %H:%M:%S'
SECONDS_PER_MINUTE = 60
MINUTES_IN_DAY = 1440
HOURS_IN_DAY = 24

def parse_date_string(date_input):
    return datetime.strptime(date_input, FORMAT_PATTERN)

def calculate_total_minutes_difference(start_date_str, end_date_str):
    start_dt = parse_date_string(start_date_str)
    end_dt = parse_date_string(end_date_str)
    time_delta = end_dt - start_dt
    days = time_delta.days
    seconds = time_delta.seconds
    total_seconds = days * HOURS_IN_DAY * 3600 + seconds
    total_minutes = total_seconds / SECONDS_PER_MINUTE
    return total_minutes

if __name__ == '__main__':
    first_sample = '2023-01-01 10:00:00'
    second_sample = '2023-01-01 12:30:00'
    minutes_diff = calculate_total_minutes_difference(first_sample, second_sample)
    print(minutes_diff)