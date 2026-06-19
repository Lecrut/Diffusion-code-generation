from datetime import timedelta, datetime

def scale_time_differences(time_diffs):
    standardized_timedeltas = []
    for time_diff in time_diffs:
        try:
            if 'day' in time_diff or 'days' in time_diff:
                days = int(time_diff.split()[0])
                td = timedelta(days=days)
            elif 'hour' in time_diff or 'hours' in time_diff:
                hours = int(time_diff.split()[0])
                td = timedelta(hours=hours)
            elif 'minute' in time_diff or 'minutes' in time_diff:
                minutes = int(time_diff.split()[0])
                td = timedelta(minutes=minutes)
            else:
                raise ValueError('Unsupported time unit')
            standardized_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_diff}': {e}")
    return standardized_timedeltas
if __name__ == '__main__':
    sample_time_differences = ['3 days', '2 hours', '45 minutes', '7 days 10 hours', 'invalid input']
    result = scale_time_differences(sample_time_differences)
    print(result)