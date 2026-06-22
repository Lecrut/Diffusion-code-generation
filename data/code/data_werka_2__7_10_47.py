class TimeUnitConverter:
    SECONDS_PER_UNIT = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2592000,
        'year': 31536000
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in TimeUnitConverter.SECONDS_PER_UNIT or to_unit not in TimeUnitConverter.SECONDS_PER_UNIT:
            raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
        
        value_in_seconds = value * TimeUnitConverter.SECONDS_PER_UNIT[from_unit]
        converted_value = value_in_seconds / TimeUnitConverter.SECONDS_PER_UNIT[to_unit]
        return converted_value

if __name__ == '__main__':
    print(TimeUnitConverter.convert(1, 'hour', 'minute'))
    print(TimeUnitConverter.convert(2, 'day', 'second'))
    print(TimeUnitConverter.convert(3, 'week', 'year'))