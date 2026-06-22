from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_deltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(' ', 1)
                hours, minutes, seconds = map(int, rest.split(':'))
                delta = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str or 'hours' in time_str:
                hours, minutes, seconds = map(int, time_str.split(':'))
                delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                minutes, seconds = map(int, time_str.split(':'))
                delta = timedelta(minutes=minutes, seconds=seconds)
            standardized_deltas.append(delta)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_deltas
if __name__ == '__main__':
    sample_time_diffs = ['2 days 3:45:00', '1 hour 30 minutes', '45:00', 'invalid time']
    result = scale_time_differences(sample_time_diffs)
    print(result)