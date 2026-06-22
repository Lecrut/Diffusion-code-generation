from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(' ', 1)
                td = timedelta(days=int(days))
            elif 'hour' in time_str or 'hours' in time_str:
                hours, rest = time_str.split(' ', 1)
                td = timedelta(hours=int(hours))
            elif 'minute' in time_str or 'minutes' in time_str:
                minutes, rest = time_str.split(' ', 1)
                td = timedelta(minutes=int(minutes))
            elif 'second' in time_str or 'seconds' in time_str:
                seconds, rest = time_str.split(' ', 1)
                td = timedelta(seconds=int(seconds))
            else:
                raise ValueError(f'Unsupported time unit in: {time_str}')
            scaled_td = td * 2
            scaled_timedeltas.append(scaled_td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return scaled_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['3 days', '4 hours', '5 minutes', '6 seconds', 'invalid input']
    result = scale_time_differences(sample_time_diffs)
    for td in result:
        print(td)