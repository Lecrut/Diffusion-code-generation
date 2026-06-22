from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {
            'd': 'days',
            'h': 'hours',
            'm': 'minutes',
            's': 'seconds'
        }

    def parse_time(self, time_str):
        try:
            value, unit = time_str[:-1], time_str[-1]
            if unit not in self.time_units:
                raise ValueError(f"Unsupported time unit: {unit}")
            return int(value), self.time_units[unit]
        except (ValueError, IndexError) as e:
            raise ValueError("Invalid time format") from e

    def summarize_durations(self, time_diffs):
        total_time = timedelta()
        for time_str in time_diffs:
            value, unit = self.parse_time(time_str)
            if unit == 'days':
                total_time += timedelta(days=value)
            elif unit == 'hours':
                total_time += timedelta(hours=value)
            elif unit == 'minutes':
                total_time += timedelta(minutes=value)
            elif unit == 'seconds':
                total_time += timedelta(seconds=value)
        
        return {
            'days': total_time.days,
            'hours': total_time.seconds // 3600,
            'minutes': (total_time.seconds % 3600) // 60,
            'seconds': total_time.seconds % 60
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['5d', '3h', '45m', '30s']
    result = time_scaler.summarize_durations(sample_times)
    print(result)