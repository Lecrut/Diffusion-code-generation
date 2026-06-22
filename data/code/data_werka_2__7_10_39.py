class TimeConverter:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400
    SECONDS_PER_WEEK = 604800
    SECONDS_PER_MONTH = 2592000
    SECONDS_PER_YEAR = 31536000

    @staticmethod
    def convert(value, from_unit, to_unit):
        time_units = {
            'second': 1,
            'minute': TimeConverter.SECONDS_PER_MINUTE,
            'hour': TimeConverter.SECONDS_PER_HOUR,
            'day': TimeConverter.SECONDS_PER_DAY,
            'week': TimeConverter.SECONDS_PER_WEEK,
            'month': TimeConverter.SECONDS_PER_MONTH,
            'year': TimeConverter.SECONDS_PER_YEAR
        }
        
        if from_unit not in time_units or to_unit not in time_units:
            raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
        
        value_in_seconds = value * time_units[from_unit]
        converted_value = value_in_seconds / time_units[to_unit]
        return converted_value

if __name__ == '__main__':
    print(TimeConverter.convert(1, 'hour', 'minute'))
    print(TimeConverter.convert(2, 'day', 'second'))
    print(TimeConverter.convert(3, 'week', 'year'))