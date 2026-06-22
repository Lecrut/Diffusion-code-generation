class TimeConverter:
    def __init__(self):
        self.conversion_factors = {
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
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        
        total_seconds = duration * self.conversion_factors[unit]
        return {
            'seconds': total_seconds,
            'minutes': total_seconds / self.conversion_factors['minutes'],
            'hours': total_seconds / self.conversion_factors['hours'],
            'days': total_seconds / self.conversion_factors['days']
        }

if __name__ == '__main__':
    converter = TimeConverter()
    sample_duration = 1
    sample_unit = 'hours'
    try:
        result = converter.convert(sample_duration, sample_unit)
        print(result)
    except ValueError as e:
        print(e)