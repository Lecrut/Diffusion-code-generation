from datetime import timedelta

class TimeScaler:

    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time_differences(self, time_diffs):
        total_seconds = 0
        for diff in time_diffs:
            if not diff[-1] in self.time_units:
                raise ValueError(f'Unsupported time unit: {diff[-1]}')
            try:
                value = int(diff[:-1])
            except ValueError:
                raise ValueError(f'Invalid number format: {diff}')
            total_seconds += value * self.time_units[diff[-1]]
        return {'days': total_seconds // 86400, 'hours': total_seconds % 86400 // 3600, 'minutes': total_seconds % 3600 // 60, 'seconds': total_seconds % 60}
if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['5d', '3h', '45m', '120s']
    result = time_scaler.parse_time_differences(sample_time_diffs)
    print(result)