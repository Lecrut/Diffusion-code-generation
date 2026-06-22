from datetime import timedelta, time

def scale_time_differences(time_diff_strings):
    parsed_timedeltas = []
    for diff_str in time_diff_strings:
        try:
            parts = diff_str.split(':')
            if len(parts) == 2:
                hours, minutes = map(int, parts)
                td = timedelta(hours=hours, minutes=minutes)
                parsed_timedeltas.append(td)
            else:
                raise ValueError('Invalid time format')
        except (ValueError, TypeError):
            parsed_timedeltas.append(None)
    return parsed_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['2:30', '4:15', 'invalid', '1:05']
    standardized_deltas = scale_time_differences(sample_time_diffs)
    print(standardized_deltas)