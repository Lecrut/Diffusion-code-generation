class TimeScaler:
    def __init__(self):
        self.unit_map = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time(self, time_str):
        if len(time_str) < 2 or not time_str[-1] in self.unit_map:
            raise ValueError("Invalid time format")
        value = time_str[:-1]
        unit = time_str[-1]
        try:
            return int(value), unit
        except ValueError:
            raise ValueError("Invalid time value")

    def summarize_durations(self, time_diffs):
        total_seconds = 0
        for time_str in time_diffs:
            value, unit = self.parse_time(time_str)
            total_seconds += value * self.unit_map[unit]
        
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['10d', '2h', '30m', '45s']
    result = time_scaler.summarize_durations(sample_times)
    print(result)