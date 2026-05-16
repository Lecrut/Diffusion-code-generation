import re
def aggregate_time_differences(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        total_seconds += parse_time_string(time_str)
    return total_seconds
def parse_time_string(time_str):
    total_seconds = 0
    parts = re.findall(r'(\d+)\s*h', time_str)
    for h in parts:
        total_seconds += int(h) * 3600
    parts = re.findall(r'(\d+)\s*m', time_str)
    for m in parts:
        total_seconds += int(m) * 60
    return total_seconds
if __name__ == '__main__':
    sample_times = [
        "1 hour 30 minutes",
        "2 hours",
        "45 minutes",
        "1 day 5 hours"
    ]
    total = aggregate_time_differences(sample_times)
    print(total)