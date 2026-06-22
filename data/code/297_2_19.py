class TimeConverter:
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def convert_seconds_to_hms(seconds):
        hours = seconds // (TimeConverter.MINUTES_PER_HOUR * TimeConverter.SECONDS_PER_MINUTE)
        minutes = seconds % (TimeConverter.MINUTES_PER_HOUR * TimeConverter.SECONDS_PER_MINUTE) // TimeConverter.SECONDS_PER_MINUTE
        remaining_seconds = seconds % TimeConverter.SECONDS_PER_MINUTE
        return f'{hours:02}:{minutes:02}:{remaining_seconds:02}'
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_seconds_to_hms(3661))