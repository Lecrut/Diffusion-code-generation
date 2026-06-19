def aggregate_durations(time_diffs):
    total_seconds = 0
    for time_str in time_diffs:
        parts = time_str.split(':')
        hours = int(parts[0]) if len(parts) > 1 else 0
        minutes = int(parts[-1])
        total_seconds += hours * 3600 + minutes * 60
    return total_seconds

if __name__ == '__main__':
    sample_durations = ["2:30", "1:45", "3:15"]
    print(aggregate_durations(sample_durations))