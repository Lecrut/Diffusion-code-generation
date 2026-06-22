from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_deltas = []
    for time_str in time_diff_strings:
        try:
            parts = time_str.split()
            total_seconds = 0
            for part in parts:
                if 'day' in part or 'days' in part:
                    days = int(part.replace('day', '').replace('s', '').strip())
                    total_seconds += days * 86400
                elif 'hour' in part or 'hours' in part:
                    hours = int(part.replace('hour', '').replace('s', '').strip())
                    total_seconds += hours * 3600
                elif 'minute' in part or 'minutes' in part:
                    minutes = int(part.replace('minute', '').replace('s', '').strip())
                    total_seconds += minutes * 60
                elif 'second' in part or 'seconds' in part:
                    seconds = int(part.replace('second', '').replace('s', '').strip())
                    total_seconds += seconds
            standardized_deltas.append(timedelta(seconds=total_seconds))
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
            standardized_deltas.append(None)
    return standardized_deltas
if __name__ == '__main__':
    sample_time_diffs = ['2 days 3 hours', '1 hour 45 minutes', '7 seconds', 'invalid time string']
    result = scale_time_differences(sample_time_diffs)
    print(result)