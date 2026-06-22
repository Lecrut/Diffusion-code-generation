class TimeConverter:
    def __init__(self):
        self.units = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }

    def convert(self, duration, unit):
        if not isinstance(duration, (int, float)):
            raise ValueError("Duration must be a number.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        if unit not in self.units:
            raise ValueError(f"Unsupported unit: {unit}")
        
        total_seconds = duration * self.units[unit]
        return {
            'seconds': total_seconds,
            'minutes': total_seconds / self.units['minutes'],
            'hours': total_seconds / self.units['hours'],
            'days': total_seconds / self.units['days']
        }

if __name__ == '__main__':
    converter = TimeConverter()
    sample_duration = 1
    sample_unit = 'hours'
    converted_time = converter.convert(sample_duration, sample_unit)
    print(converted_time)