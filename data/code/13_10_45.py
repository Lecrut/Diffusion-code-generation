from datetime import timedelta

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    for time_str in time_diff_strings:
        try:
            parts = time_str.split()
            if len(parts) != 2:
                raise ValueError(f'Invalid format: {time_str}')
            value = float(parts[0])
            unit = parts[1].lower()
            if unit == 'seconds':
                td = timedelta(seconds=value)
            elif unit == 'minutes':
                td = timedelta(minutes=value)
            elif unit == 'hours':
                td = timedelta(hours=value)
            elif unit == 'days':
                td = timedelta(days=value)
            else:
                raise ValueError(f'Unsupported unit: {unit}')
            standardized_timedeltas.append(td)
        except (ValueError, IndexError) as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_timedeltas
if __name__ == '__main__':
    sample_time_differences = ['30 seconds', '1.5 minutes', '2 hours', '4 days', 'invalid input']
    result = scale_time_differences(sample_time_differences)
    print(result)