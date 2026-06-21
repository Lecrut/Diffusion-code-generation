from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str:
                days, rest = time_str.split(' day')
                hours, minutes, seconds = map(int, rest.strip().split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str:
                hours, minutes, seconds = map(int, time_str.strip().split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                raise ValueError(f'Unsupported time format: {time_str}')
            scaled_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return scaled_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 12:30:45', '2 days 08:15:30', '7 hours 45:00', 'invalid time']
    result = scale_time_differences(sample_time_diffs)
    for td in result:
        print(td)