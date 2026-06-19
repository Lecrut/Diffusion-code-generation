def aggregate_durations(durations):
    total_seconds = 0
    for duration in durations:
        parts = duration.split()
        for part in parts:
            if 'h' in part:
                hours = int(part.replace('h', ''))
                total_seconds += hours * 3600
            elif 'm' in part:
                minutes = int(part.replace('m', ''))
                total_seconds += minutes * 60
    return total_seconds

if __name__ == '__main__':
    sample_durations = ["2h 30m", "1h 45m", "30m"]
    print(aggregate_durations(sample_durations))