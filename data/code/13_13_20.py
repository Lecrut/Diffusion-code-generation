def aggregate_durations(time_diffs):
    total_seconds = 0
    for time_str in time_diffs:
        parts = time_str.split()
        for part in parts:
            if 'h' in part:
                hours = int(part.replace('h', ''))
                total_seconds += hours * 3600
            elif 'm' in part:
                minutes = int(part.replace('m', ''))
                total_seconds += minutes * 60
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = ["2h 30m", "1h 45m", "30m"]
    print(aggregate_durations(sample_time_diffs))