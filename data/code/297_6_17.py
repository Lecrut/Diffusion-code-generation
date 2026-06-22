class TimeConverter:
    SECONDS_PER_HOUR = 3600
    MILLISECONDS_PER_SECOND = 1000

    @staticmethod
    def hours_to_milliseconds(hours):
        return int(hours * TimeConverter.SECONDS_PER_HOUR * TimeConverter.MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    converter = TimeConverter()
    print(f"2 hours is {converter.hours_to_milliseconds(2)} milliseconds")
    print(f"5 hours is {converter.hours_to_milliseconds(5)} milliseconds")