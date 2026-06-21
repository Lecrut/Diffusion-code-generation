def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for time_diff in time_diffs:
        if 'h' in time_diff and 'm' in time_diff:
            hours, minutes = map(int, time_diff.split('h'))
            total_seconds += (hours * 3600) + (minutes * 60)
        elif 'h' in time_diff:
            hours = int(time_diff.replace('h', ''))
            total_seconds += hours * 3600
        elif 'm' in time_diff:
            minutes = int(time_diff.replace('m', ''))
            total_seconds += minutes * 60
        else:
            raise ValueError(f"Unsupported format: {time_diff}")
    return total_seconds

if __name__ == '__main__':
    sample_time_differences = ['2h30m', '1h45m', '30m']
    total_duration_seconds = aggregate_time_differences(sample_time_differences)
    print(total_duration_seconds)