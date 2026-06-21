from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {
            'day': 86400,
            'hour': 3600,
            'minute': 60,
            'second': 1
        }

    def parse_time_differences(self, time_diffs):
        total_seconds = 0
        for diff in time_diffs:
            value, unit = diff.split()
            value = int(value)
            if unit.endswith('s'):
                unit = unit[:-1]
            if unit not in self.time_units:
                raise ValueError(f"Unsupported time unit: {unit}")
            total_seconds += value * self.time_units[unit]

        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['2 days', '5 hours', '30 minutes', '45 seconds']
    result = time_scaler.parse_time_differences(sample_time_diffs)
    print(result)