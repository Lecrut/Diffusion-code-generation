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
            value = int(parts[0])
            unit = parts[1]
            if unit == 'd':
                self.time_units['days'] += value
            elif unit == 'h':
                self.time_units['hours'] += value
            elif unit == 'm':
                self.time_units['minutes'] += value
            elif unit == 's':
                self.time_units['seconds'] += value

    def total_duration(self):
        td = timedelta(days=self.time_units['days'],
                      hours=self.time_units['hours'],
                      minutes=self.time_units['minutes'],
                      seconds=self.time_units['seconds'])
        return {
            'total_seconds': int(td.total_seconds()),
            'days': td.days,
            'hours': td.seconds // 3600,
            'minutes': (td.seconds % 3600) // 60,
            'seconds': td.seconds % 60
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['5d', '3h', '45m', '120s']
    time_scaler.parse_time_differences(sample_time_diffs)
    print(time_scaler.total_duration())