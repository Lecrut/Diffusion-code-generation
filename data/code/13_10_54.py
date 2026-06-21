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
                parts = time_str.split(':')
                if len(parts) == 3:
                    hours, minutes, seconds = map(int, parts)
                else:
                    hours = int(parts[0])
                    minutes = int(parts[1]) if len(parts) > 1 else 0
                    seconds = int(parts[2]) if len(parts) > 2 else 0
                delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            elif 'minute' in time_str or 'minutes' in time_str:
                parts = time_str.split(':')
                if len(parts) == 2:
                    minutes, seconds = map(int, parts)
                else:
                    minutes = int(parts[0])
                    seconds = int(parts[1]) if len(parts) > 1 else 0
                delta = timedelta(minutes=minutes, seconds=seconds)
            elif 'second' in time_str or 'seconds' in time_str:
                seconds = int(time_str.split(' ')[0])
                delta = timedelta(seconds=seconds)
            else:
                raise ValueError(f'Unsupported time format: {time_str}')
            standardized_deltas.append(delta)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_deltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2 hours 30 minutes 45 seconds', '2 hours 30 minutes', '45 minutes 30 seconds', '100 seconds', 'invalid time format']
    result = scale_time_differences(sample_time_diffs)
    print(result)