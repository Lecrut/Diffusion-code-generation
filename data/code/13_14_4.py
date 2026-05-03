import re
def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for diff_str in time_diffs:
        total_seconds += parse_time_difference(diff_str)
    return total_seconds
def parse_time_difference(diff_str):
    total_seconds = 0
    parts = re.findall(r'(\d+)\s*h', diff_str)
    if parts:
        total_seconds += sum(int(p) for p in parts) * 3600
    parts = re.findall(r'(\d+)\s*m', diff_str)
    if parts:
        total_seconds += sum(int(p) for p in parts) * 60
    return total_seconds
if __name__ == '__main__':
    sample_differences = [
        "1 hour 30 minutes",
        "2 hours",
        "45 minutes",
        "1 day 5 hours"
    ]
    total = aggregate_time_differences(sample_differences)
    print(total)