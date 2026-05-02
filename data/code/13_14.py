import re
def aggregate_time_differences(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        total_seconds += parse_time_string(time_str)
    return total_seconds
def parse_time_string(time_str):
    total_seconds = 0
    parts = re.findall(r'(\d+)\s*h', time_str)
    if parts:
        for h in parts:
            total_seconds += int(h) * 3600
    parts = re.findall(r'(\d+)\s*m', time_str)
    if parts:
        for m in parts:
            total_seconds += int(m) * 60
    return total_seconds
if __name__ == '__main__':
    sample_times = [
        "2h 30m",
        "1h",
        "45m",
        "10h 15m",
        "5m"
    ]
    total = aggregate_time_differences(sample_times)
    print(total)