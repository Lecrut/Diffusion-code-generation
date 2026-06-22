from datetime import timedelta

class TimeScaler:

    def __init__(self):
        self.durations = {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    def parse_time_differences(self, time_diffs):
        for td_str in time_diffs:
            self._parse_single_time_difference(td_str)

    def _parse_single_time_difference(self, td_str):
        parts = td_str.split(':')
        if len(parts) == 4:
            days, hours, minutes, seconds = map(int, parts)
        elif len(parts) == 3:
            days, hours, minutes, seconds = (0, int(parts[0]), int(parts[1]), int(parts[2]))
        elif len(parts) == 2:
            days, hours, minutes, seconds = (0, 0, int(parts[0]), int(parts[1]))
        else:
            raise ValueError('Invalid time difference format')
        self.durations['days'] += days
        self.durations['hours'] += hours
        self.durations['minutes'] += minutes
        self.durations['seconds'] += seconds

    def get_total_duration(self):
        total_seconds = self.durations['days'] * 86400 + self.durations['hours'] * 3600 + self.durations['minutes'] * 60 + self.durations['seconds']
        return total_seconds
if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['2:30:45', '1:05', '3600', '2:10:30:15']
    time_scaler.parse_time_differences(sample_time_diffs)
    total_seconds = time_scaler.get_total_duration()
    print(f'Total duration in seconds: {total_seconds}')