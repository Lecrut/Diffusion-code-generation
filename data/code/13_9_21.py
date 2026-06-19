from dateutil import parser

def parse_time_difference(time_str):
    parsed = parser.parse(time_str, fuzzy=True)
    total_seconds = parsed.total_seconds()
    return int(total_seconds / 60)

def calculate_total_elapsed_time(time_differences):
    total_minutes = sum((parse_time_difference(time_diff) for time_diff in time_differences))
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '1 hour']
    total_minutes = calculate_total_elapsed_time(sample_times)
    print(total_minutes)