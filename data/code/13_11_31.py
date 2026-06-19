from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(' ', 1)
                hours, minutes, seconds = map(int, rest.split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str or 'hours' in time_str:
                parts = time_str.split(':')
                if len(parts) == 3:
                    hours, minutes, seconds = map(int, parts)
                else:
                    hours, minutes = map(int, parts)
                    seconds = 0
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            elif 'minute' in time_str or 'minutes' in time_str:
                parts = time_str.split(':')
                if len(parts) == 2:
                    minutes, seconds = map(int, parts)
                else:
                    minutes = int(parts[0])
                    seconds = 0
                td = timedelta(minutes=minutes, seconds=seconds)
            elif 'second' in time_str or 'seconds' in time_str:
                seconds = int(time_str.split(' ')[0])
                td = timedelta(seconds=seconds)
            else:
                raise ValueError('Unsupported time format')
            standardized_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '3 hours 45 minutes', '100 seconds', 'invalid time string']
    result = scale_time_differences(sample_time_diffs)
    print(result)