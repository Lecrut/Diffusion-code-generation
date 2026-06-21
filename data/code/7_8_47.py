class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24

    @staticmethod
    def convert_time(duration, unit):
        if not isinstance(duration, (int, float)):
            raise ValueError("Duration must be a number.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")

        supported_units = {
            'seconds': 1,
            'minutes': TimeConverter.SECONDS_IN_MINUTE,
            'hours': TimeConverter.MINUTES_IN_HOUR * TimeConverter.SECONDS_IN_MINUTE,
            'days': TimeConverter.HOURS_IN_DAY * TimeConverter.MINUTES_IN_HOUR * TimeConverter.SECONDS_IN_MINUTE
        }

        if unit not in supported_units:
            raise ValueError(f"Unsupported unit: {unit}")

        total_seconds = duration * supported_units[unit]
        return {
            'seconds': total_seconds,
            'minutes': total_seconds / supported_units['minutes'],
            'hours': total_seconds / supported_units['hours'],
            'days': total_seconds / supported_units['days']
        }

if __name__ == '__main__':
    sample_duration = 1
    sample_unit = 'hours'
    try:
        converted_times = TimeConverter.convert_time(sample_duration, sample_unit)
        print(converted_times)
    except ValueError as e:
        print(e)