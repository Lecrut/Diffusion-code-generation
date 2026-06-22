def parse_time_difference(time_str):
    hours, minutes = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60

def aggregate_durations(time_diffs):
    total_seconds = sum(parse_time_difference(td) for td in time_diffs)
    return total_seconds

if __name__ == '__main__':
    sample_times = ["2:30", "1:45", "3:15"]
    print(aggregate_durations(sample_times))