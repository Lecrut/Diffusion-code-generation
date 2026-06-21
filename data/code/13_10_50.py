from datetime import timedelta

def scale_time_differences(time_diff_strings):
    time_deltas = []
    for diff_str in time_diff_strings:
        try:
            if 'day' in diff_str:
                days, rest = diff_str.split(' day')
                hours, minutes, seconds = map(int, rest.strip().split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in diff_str:
                hours, minutes, seconds = map(int, diff_str.strip().split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                raise ValueError(f'Unsupported time difference format: {diff_str}')
            time_deltas.append(td)
        except Exception as e:
            print(f"Error parsing '{diff_str}': {e}")
    return time_deltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 12:30:45', '2 days 08:15:00', '3 hours 45 minutes 30 seconds', 'invalid format']
    standardized_deltas = scale_time_differences(sample_time_diffs)
    for delta in standardized_deltas:
        print(delta)