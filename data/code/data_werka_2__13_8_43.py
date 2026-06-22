import re

def parse_time_difference(time_str):
    hours_match = re.search('(\\d+)\\s*hours?', time_str)
    minutes_match = re.search('(\\d+)\\s*minutes?', time_str)
    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0
    return hours * 60 + minutes

def total_elapsed_time(time_differences):
    total_minutes = sum((parse_time_difference(td) for td in time_differences))
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes']
    print(total_elapsed_time(sample_times))