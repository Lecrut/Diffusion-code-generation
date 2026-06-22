from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {
            'days': 0,
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }

    def parse_time_differences(self, time_diffs):
        for diff in time_diffs:
            parts = diff.split()
            for part in parts:
                if 'day' in part:
                    self.time_units['days'] += int(part.replace('day', '').replace('s', ''))
                elif 'hour' in part:
                    self.time_units['hours'] += int(part.replace('hour', '').replace('s', ''))
                elif 'minute' in part:
                    self.time_units['minutes'] += int(part.replace('minute', '').replace('s', ''))
                elif 'second' in part:
                    self.time_units['seconds'] += int(part.replace('second', '').replace('s', ''))

    def get_total_duration(self):
        total_seconds = (self.time_units['days'] * 86400 +
                        self.time_units['hours'] * 3600 +
                        self.time_units['minutes'] * 60 +
                        self.time_units['seconds'])
        return timedelta(seconds=total_seconds)

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = [
        "2 days 5 hours",
        "3 hours 45 minutes",
        "1 hour 30 seconds",
        "7 days"
    ]
    time_scaler.parse_time_differences(sample_time_diffs)
    total_duration = time_scaler.get_total_duration()
    print(total_duration)