from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str:
                days, remainder = time_str.split(' day')
                hours, minutes, seconds = map(int, remainder.strip().split(':'))
                td = timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str:
                hours, minutes, seconds = map(int, time_str.strip().split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                hours, minutes, seconds = map(int, time_str.strip().split(':'))
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            scaled_timedeltas.append(td)
        except Exception as e:
            scaled_timedeltas.append(None)
    return scaled_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['1 day 2:30:45', '3:45:67', 'invalid time string', '2 days 10:20:30']
    result = scale_time_differences(sample_time_diffs)
    print(result)