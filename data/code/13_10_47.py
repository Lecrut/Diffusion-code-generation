from datetime import timedelta

def scale_time_differences(time_diff_strings):
    time_deltas = []
    for diff_str in time_diff_strings:
        try:
            if 'day' in diff_str or 'days' in diff_str:
                days, rest = diff_str.split(' ', 1)
                td = timedelta(days=int(days))
            elif 'hour' in diff_str or 'hours' in diff_str:
                hours, rest = diff_str.split(' ', 1)
                td = timedelta(hours=int(hours))
            elif 'minute' in diff_str or 'minutes' in diff_str:
                minutes, rest = diff_str.split(' ', 1)
                td = timedelta(minutes=int(minutes))
            else:
                raise ValueError(f'Unsupported time unit in: {diff_str}')
            time_deltas.append(td)
        except Exception as e:
            print(f"Error parsing '{diff_str}': {e}")
    return time_deltas
if __name__ == '__main__':
    sample_time_diffs = ['5 days', '3 hours', '45 minutes', 'invalid input']
    result = scale_time_differences(sample_time_diffs)
    print(result)