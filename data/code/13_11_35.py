from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    for time_str in time_diff_strings:
        try:
            if 'day' in time_str or 'days' in time_str:
                days, rest = time_str.split(',')
                days = int(days.strip().split()[0])
                hours, minutes, seconds = map(int, rest.strip().split(','))
                td = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
            elif 'hour' in time_str or 'hours' in time_str:
                parts = time_str.split(',')
                hours = int(parts[0].strip().split()[0])
                minutes = int(parts[1].strip().split()[0]) if len(parts) > 1 else 0
                seconds = int(parts[2].strip().split()[0]) if len(parts) > 2 else 0
                td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            elif 'minute' in time_str or 'minutes' in time_str:
                parts = time_str.split(',')
                minutes = int(parts[0].strip().split()[0])
                seconds = int(parts[1].strip().split()[0]) if len(parts) > 1 else 0
                td = timedelta(minutes=minutes, seconds=seconds)
            elif 'second' in time_str or 'seconds' in time_str:
                parts = time_str.split(',')
                seconds = int(parts[0].strip().split()[0])
                td = timedelta(seconds=seconds)
            standardized_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['2 days, 3 hours, 45 minutes, 10 seconds', '5 hours, 20 minutes, 30 seconds', '1 hour, 30 minutes', '45 minutes, 15 seconds', '10 seconds']
    result = scale_time_differences(sample_time_diffs)
    for td in result:
        print(td)