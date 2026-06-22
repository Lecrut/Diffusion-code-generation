from datetime import timedelta

def scale_time_differences(time_diff_strings):
    scaled_timedeltas = []
    for time_str in time_diff_strings:
        try:
            hours, minutes, seconds = map(int, time_str.split(':'))
            td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            scaled_timedeltas.append(td)
        except ValueError:
            print(f"Error parsing time string '{time_str}': Invalid format.")
            scaled_timedeltas.append(None)
    return scaled_timedeltas
if __name__ == '__main__':
    sample_time_diffs = ['01:30:45', '2:45:10', 'invalid_time', '00:00:00']
    result = scale_time_differences(sample_time_diffs)
    print(result)