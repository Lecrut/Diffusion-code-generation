from datetime import timedelta, time

def scale_time_differences(time_diffs):
    standardized_deltas = []
    for diff_str in time_diffs:
        try:
            parts = diff_str.split(':')
            if len(parts) != 2:
                raise ValueError('Invalid time format')
            hours, minutes = map(int, parts)
            delta = timedelta(hours=hours, minutes=minutes)
            standardized_deltas.append(delta)
        except (ValueError, TypeError):
            standardized_deltas.append(None)
    return standardized_deltas
if __name__ == '__main__':
    sample_time_diffs = ['2:30', '1:45', 'invalid', '3:60', '0:15']
    result = scale_time_differences(sample_time_diffs)
    print(result)