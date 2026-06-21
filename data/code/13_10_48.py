from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_durations = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str:
                days, rest = time_str.split(' day')
                hours, minutes, seconds = map(int, rest.strip().split(':'))
                scaled_durations.append(timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds))
            elif 'hour' in time_str:
                hours, minutes, seconds = map(int, time_str.strip().split(':'))
                scaled_durations.append(timedelta(hours=hours, minutes=minutes, seconds=seconds))
            else:
                raise ValueError(f'Unsupported time format: {time_str}')
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
            scaled_durations.append(None)
    return scaled_durations
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '3 hours 45 minutes', 'invalid time string']
    print(scale_time_differences(sample_time_diffs))