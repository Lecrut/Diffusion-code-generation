from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time(self, time_str):
        if len(time_str) < 2 or not time_str[-1] in self.time_units:
            raise ValueError("Invalid time format")
        value = int(time_str[:-1])
        unit = time_str[-1]
        return value * self.time_units[unit]

    def summarize_durations(self, time_diffs):
        total_seconds = sum(self.parse_time(time) for time in time_diffs)
        td = timedelta(seconds=total_seconds)
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['2d', '7h', '30m', '45s']
    result = time_scaler.summarize_durations(sample_times)
    print(result)