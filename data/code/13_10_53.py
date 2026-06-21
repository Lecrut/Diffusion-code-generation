from datetime import timedelta
import re

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    time_pattern = re.compile(r'(\d+)([dhms])')

    for diff_str in time_diff_strings:
        try:
            total_seconds = 0
            matches = time_pattern.findall(diff_str)
            if not matches:
                raise ValueError(f"Invalid time difference format: {diff_str}")

            for value, unit in matches:
                value = int(value)
                if unit == 'd':
                    total_seconds += value * 86400
                elif unit == 'h':
                    total_seconds += value * 3600
                elif unit == 'm':
                    total_seconds += value * 60
                elif unit == 's':
                    total_seconds += value
                else:
                    raise ValueError(f"Unsupported time unit: {unit}")

            standardized_timedeltas.append(timedelta(seconds=total_seconds))

        except Exception as e:
            print(f"Error processing '{diff_str}': {e}")
            standardized_timedeltas.append(None)

    return standardized_timedeltas

if __name__ == '__main__':
    sample_time_diffs = ['2d3h', '1m45s', '7h', 'invalid', '3d']
    result = scale_time_differences(sample_time_diffs)
    print(result)