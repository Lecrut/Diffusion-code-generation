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
        
        seconds = duration * self.conversion_factors[unit]
        return {
            'seconds': seconds,
            'minutes': seconds / self.conversion_factors['minutes'],
            'hours': seconds / self.conversion_factors['hours'],
            'days': seconds / self.conversion_factors['days']
        }

if __name__ == '__main__':
    converter = TimeConverter()
    sample_duration = 1
    for unit in ['seconds', 'minutes', 'hours', 'days']:
        print(converter.convert(sample_duration, unit))