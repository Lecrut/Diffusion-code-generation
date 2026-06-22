from datetime import datetime

def get_difference_in_minutes(date_string_one, date_string_two):
    format_pattern = '%Y-%m-%d %H:%M:%S'
    first_timestamp = datetime.strptime(date_string_one, format_pattern)
    second_timestamp = datetime.strptime(date_string_two, format_pattern)
    time_span = second_timestamp - first_timestamp
    total_seconds_elapsed = time_span.total_seconds()
    minutes_elapsed = total_seconds_elapsed / 60
    return minutes_elapsed

if __name__ == '__main__':
    first_sample = '2024-05-10 08:15:00'
    second_sample = '2024-05-10 09:45:00'
    calculated_minutes = get_difference_in_minutes(first_sample, second_sample)
    print(calculated_minutes)