from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {
            'days': 86400,
            'hours': 3600,
            'minutes': 60,
            'seconds': 1
        }

    def parse_time_differences(self, time_diffs):
        total_seconds = 0
        for diff in time_diffs:
            value, unit = diff.split()
            value = int(value)
            if unit not in self.time_units:
                raise ValueError(f"Unsupported time unit: {unit}")
            total_seconds += value * self.time_units[unit]
        
        return {
            'days': total_seconds // 86400,
            'hours': (total_seconds % 86400) // 3600,
            'minutes': (total_seconds % 3600) // 60,
            'seconds': total_seconds % 60
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['2 days', '5 hours', '30 minutes', '45 seconds']
    result = time_scaler.parse_time_differences(sample_time_diffs)
    print(result)