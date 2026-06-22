from datetime import timedelta

def scale_time_differences(time_diff_strings):
    time_deltas = []
    for diff_str in time_diff_strings:
        try:
            if 'day' in diff_str:
                days, rest = diff_str.split(' day')
                hours, minutes, seconds = map(int, rest.split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in diff_str:
                hours, minutes, seconds = map(int, diff_str.split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                raise ValueError(f'Unsupported time difference format: {diff_str}')
            time_deltas.append(td)
        except Exception as e:
            print(f"Error parsing '{diff_str}': {e}")
    return time_deltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '2 hours 45 minutes', 'invalid format']
    result = scale_time_differences(sample_time_diffs)
    print(result)