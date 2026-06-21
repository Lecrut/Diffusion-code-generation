from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    def parse_time(self, time_str):
        try:
            parts = time_str.split()
            for part in parts:
                if 'day' in part:
                    self.time_units['days'] += int(part.replace('day', '').replace('s', ''))
                elif 'hour' in part:
                    self.time_units['hours'] += int(part.replace('hour', '').replace('s', ''))
                elif 'minute' in part:
                    self.time_units['minutes'] += int(part.replace('minute', '').replace('s', ''))
                elif 'second' in part:
                    self.time_units['seconds'] += int(part.replace('second', '').replace('s', ''))
        except ValueError as e:
            raise ValueError(f"Invalid time string: {time_str}") from e

    def summarize(self, time_diff_list):
        for time_str in time_diff_list:
            self.parse_time(time_str)
        total_seconds = (self.time_units['days'] * 86400 +
                        self.time_units['hours'] * 3600 +
                        self.time_units['minutes'] * 60 +
                        self.time_units['seconds'])
        return {
            'total_days': self.time_units['days'],
            'total_hours': self.time_units['hours'],
            'total_minutes': self.time_units['minutes'],
            'total_seconds': self.time_units['seconds'],
            'total_duration': str(timedelta(seconds=total_seconds))
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = [
        "3 days 5 hours",
        "2 hours 45 minutes",
        "10 minutes 30 seconds"
    ]
    result = time_scaler.summarize(sample_times)
    print(result)