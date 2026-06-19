from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str:
                days, rest = time_str.split(' day')
                hours, minutes, seconds = map(int, rest.split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str:
                hours, minutes, seconds = map(int, time_str.split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                raise ValueError('Unsupported time format')
            standardized_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '3 hours 45 minutes 30 seconds', 'invalid time string']
    result = scale_time_differences(sample_time_diffs)
    print(result)