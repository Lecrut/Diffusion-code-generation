class TimeConverter:
    HOURS_TO_MINUTES = 60
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    @staticmethod
    def hours_to_minutes(hours):
        return hours * TimeConverter.HOURS_TO_MINUTES

    @staticmethod
    def hours_to_seconds(hours):
        return hours * TimeConverter.HOURS_TO_SECONDS

    @staticmethod
    def minutes_to_hours(minutes):
        return minutes / TimeConverter.HOURS_TO_MINUTES

    @staticmethod
    def minutes_to_seconds(minutes):
        return minutes * TimeConverter.MINUTES_TO_SECONDS

    @staticmethod
    def seconds_to_hours(seconds):
        return seconds / TimeConverter.HOURS_TO_SECONDS

    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds / TimeConverter.MINUTES_TO_SECONDS

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'h' and to_unit == 'm':
            return self.hours_to_minutes(value)
        if from_unit == 'h' and to_unit == 's':
            return self.hours_to_seconds(value)
        if from_unit == 'm' and to_unit == 'h':
            return self.minutes_to_hours(value)
        if from_unit == 'm' and to_unit == 's':
            return self.minutes_to_seconds(value)
        if from_unit == 's' and to_unit == 'h':
            return self.seconds_to_hours(value)
        if from_unit == 's' and to_unit == 'm':
            return self.seconds_to_minutes(value)
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.hours_to_minutes(3))
    print(converter.seconds_to_hours(7200))
    print(converter.convert(1.5, 'h', 's'))
    print(converter.convert(90, 'm', 'h'))