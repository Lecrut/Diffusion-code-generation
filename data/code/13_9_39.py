from datetime import timedelta

class TimeScaler:

    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time_differences(self, time_diff_strings):
        total_seconds = 0
        for time_str in time_diff_strings:
            if not time_str[-1] in self.time_units:
                raise ValueError(f'Unsupported time unit in {time_str}')
            try:
                value = int(time_str[:-1])
            except ValueError:
                raise ValueError(f'Invalid number format in {time_str}')
            total_seconds += value * self.time_units[time_str[-1]]
        td = timedelta(seconds=total_seconds)
        return {'days': td.days, 'hours': td.seconds // 3600, 'minutes': td.seconds % 3600 // 60, 'seconds': td.seconds % 60}
if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['5d', '3h', '45m', '120s']
    result = time_scaler.parse_time_differences(sample_time_diffs)
    print(result)