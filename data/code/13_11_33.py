from datetime import timedelta, datetime

def scale_time_differences(time_diff_strings):
    standardized_deltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days = int(time_str.split()[0])
                delta = timedelta(days=days)
            elif 'hour' in time_str or 'hours' in time_str:
                hours = int(time_str.split()[0])
                delta = timedelta(hours=hours)
            elif 'minute' in time_str or 'minutes' in time_str:
                minutes = int(time_str.split()[0])
                delta = timedelta(minutes=minutes)
            else:
                raise ValueError('Unsupported time unit')
            standardized_deltas.append(delta)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_deltas
if __name__ == '__main__':
    sample_time_diffs = ['5 days', '3 hours', '45 minutes', 'invalid time']
    result = scale_time_differences(sample_time_diffs)
    print(result)