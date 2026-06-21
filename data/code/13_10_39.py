from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_differences = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(' ', 1)
                hours, minutes, seconds = map(int, rest.split(':'))
                scaled_differences.append(timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds))
            elif 'hour' in time_str or 'hours' in time_str:
                hours, minutes, seconds = map(int, time_str.split(':'))
                scaled_differences.append(timedelta(hours=hours, minutes=minutes, seconds=seconds))
            elif 'minute' in time_str or 'minutes' in time_str:
                minutes, seconds = map(int, time_str.split(':'))
                scaled_differences.append(timedelta(minutes=minutes, seconds=seconds))
            elif 'second' in time_str or 'seconds' in time_str:
                seconds = int(time_str)
                scaled_differences.append(timedelta(seconds=seconds))
            else:
                raise ValueError(f'Unsupported time difference format: {time_str}')
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
            scaled_differences.append(None)
    return scaled_differences
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '3 hours 45 minutes', '10 minutes 30 seconds', '60 seconds', 'invalid time format']
    print(scale_time_differences(sample_time_diffs))