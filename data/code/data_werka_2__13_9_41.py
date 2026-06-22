class TimeScaler:

    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time_differences(self, time_diff_strings):
        total_seconds = 0
        for time_str in time_diff_strings:
            if not time_str[-1] in self.time_units:
                raise ValueError(f'Unsupported time unit in {time_str}')
            value = int(time_str[:-1])
            unit = time_str[-1]
            total_seconds += value * self.time_units[unit]
        return self._seconds_to_summary(total_seconds)

    def _seconds_to_summary(self, total_seconds):
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['5d', '3h', '45m', '12s']
    result = time_scaler.parse_time_differences(sample_times)
    print(result)
    another_sample_times = ['2d', '6h', '10m', '30s']
    another_result = time_scaler.parse_time_differences(another_sample_times)
    print(another_result)