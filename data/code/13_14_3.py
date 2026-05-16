def aggregate_time_differences(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        parts = time_str.split()
        if len(parts) == 2:
            value = int(parts[0])
            unit = parts[1]
            if unit == 'hours':
                total_seconds += value * 3600
            elif unit == 'minutes':
                total_seconds += value * 60
        else:
            continue
    return total_seconds
if __name__ == '__main__':
    sample_times = [
        "1 hour 30 minutes",
        "2 hours",
        "45 minutes",
        "1 hour 15 minutes",
        "30 minutes"
    ]
    total = aggregate_time_differences(sample_times)
    print(total)