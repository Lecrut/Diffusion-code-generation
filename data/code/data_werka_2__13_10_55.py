from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_differences = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(' ', 1)
                hours, minutes, seconds = map(int, rest.split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str or 'hours' in time_str:
                hours, minutes, seconds = map(int, time_str.split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            elif 'minute' in time_str or 'minutes' in time_str:
                minutes, seconds = map(int, time_str.split(':'))
                td = timedelta(minutes=minutes, seconds=seconds)
            elif 'second' in time_str or 'seconds' in time_str:
                seconds = int(time_str.split(':')[0])
                td = timedelta(seconds=seconds)
            else:
                raise ValueError(f'Unsupported time format: {time_str}')
            scaled_differences.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return scaled_differences
if __name__ == '__main__':
    sample_time_diffs = ['2 days 10:30:45', '5 hours 30 minutes', '20 minutes 15 seconds', '60 seconds', 'invalid time']
    result = scale_time_differences(sample_time_diffs)
    for td in result:
        print(td)