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

    def total_duration(self):
        td = timedelta(days=self.time_units['days'],
                      hours=self.time_units['hours'],
                      minutes=self.time_units['minutes'],
                      seconds=self.time_units['seconds'])
        return {
            'total_seconds': td.total_seconds(),
            'days': self.time_units['days'],
            'hours': self.time_units['hours'],
            'minutes': self.time_units['minutes'],
            'seconds': self.time_units['seconds']
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = [
        "3 days 5 hours",
        "2 hours 45 minutes",
        "10 seconds",
        "1 day"
    ]
    time_scaler.parse_time_differences(sample_time_diffs)
    print(time_scaler.total_duration())