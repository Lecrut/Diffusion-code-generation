class TimeConverter:
    SECONDS_PER_HOUR = 3600
    MILLISECONDS_PER_SECOND = 1000

    @staticmethod
    def hours_to_milliseconds(hours):
        return int(hours * TimeConverter.SECONDS_PER_HOUR * TimeConverter.MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {converter.hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {converter.hours_to_milliseconds(sample_hours_2)} milliseconds")