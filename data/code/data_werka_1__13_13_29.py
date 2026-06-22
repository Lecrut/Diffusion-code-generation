def aggregate_durations(time_diffs):
    total_seconds = 0
    for time_str in time_diffs:
        if 'h' in time_str and 'm' in time_str:
            hours, minutes = map(int, time_str.split('h'))
            total_seconds += (hours * 3600) + (minutes * 60)
        elif 'h' in time_str:
            hours = int(time_str.replace('h', ''))
            total_seconds += hours * 3600
        elif 'm' in time_str:
            minutes = int(time_str.replace('m', ''))
            total_seconds += minutes * 60
    return total_seconds

if __name__ == '__main__':
    sample_times = ['2h30m', '1h45m', '30m', '1h']
    print(aggregate_durations(sample_times))