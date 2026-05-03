def aggregate_time_differences(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        parts = time_str.split()
        if not parts:
            continue
        value = 0
        unit = ""
        if len(parts) == 2:
            try:
                value = int(parts[0])
                unit = parts[1]
            except ValueError:
                continue
        elif len(parts) == 1:
            try:
                value = int(parts[0])
                unit = "seconds"
            except ValueError:
                continue
        else:
            continue
        if unit == "hours":
            total_seconds += value * 3600
        elif unit == "minutes":
            total_seconds += value * 60
        elif unit == "seconds":
            total_seconds += value
    return total_seconds
if __name__ == '__main__':
    sample_times = [
        "1 hour 30 minutes",
        "2 hours",
        "45 minutes",
        "120 seconds",
        "5 hours 15 minutes"
    ]
    total = aggregate_time_differences(sample_times)
    print(total)