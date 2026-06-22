class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    SUPPORTED_UNITS = {
        'seconds': 1,
        'minutes': SECONDS_PER_MINUTE,
        'hours': MINUTES_PER_HOUR * SECONDS_PER_MINUTE,
        'days': HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    }

    @staticmethod
    def convert(duration, unit):
        if not isinstance(duration, (int, float)):
            raise ValueError("Duration must be a number.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        if unit not in TimeConverter.SUPPORTED_UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
        
        total_seconds = duration * TimeConverter.SUPPORTED_UNITS[unit]
        return {
            'seconds': total_seconds,
            'minutes': total_seconds / TimeConverter.SECONDS_PER_MINUTE,
            'hours': total_seconds / (TimeConverter.MINUTES_PER_HOUR * TimeConverter.SECONDS_PER_MINUTE),
            'days': total_seconds / (TimeConverter.HOURS_PER_DAY * TimeConverter.MINUTES_PER_HOUR * TimeConverter.SECONDS_PER_MINUTE)
        }

if __name__ == '__main__':
    sample_duration = 1
    sample_unit = 'hours'
    converted_time = TimeConverter.convert(sample_duration, sample_unit)
    print(converted_time)