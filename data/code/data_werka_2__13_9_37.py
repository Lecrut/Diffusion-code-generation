class TimeScaler:
    DAY_SECONDS = 86400
    HOUR_SECONDS = 3600
    MINUTE_SECONDS = 60

    def __init__(self):
        self.time_units = {
            'd': self.DAY_SECONDS,
            'h': self.HOUR_SECONDS,
            'm': self.MINUTE_SECONDS,
            's': 1
        }

    def parse_time_differences(self, time_diff_strings):
        total_seconds = 0
        for time_str in time_diff_strings:
            if not time_str[-1] in self.time_units:
                raise ValueError(f'Unsupported time unit in {time_str}')
            value = int(time_str[:-1])
            unit = time_str[-1]
            total_seconds += value * self.time_units[unit]
        
        return self._summarize_durations(total_seconds)

    def _summarize_durations(self, total_seconds):
        days = total_seconds // self.DAY_SECONDS
        remaining_seconds = total_seconds % self.DAY_SECONDS
        hours = remaining_seconds // self.HOUR_SECONDS
        remaining_seconds %= self.HOUR_SECONDS
        minutes = remaining_seconds // self.MINUTE_SECONDS
        seconds = remaining_seconds % self.MINUTE_SECONDS
        
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['5d', '3h', '45m', '12s']
    result = time_scaler.parse_time_differences(sample_times)
    print(result)