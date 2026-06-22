class TimeConverter:
    SECONDS_PER_HOUR = 3600
    MILLISECONDS_PER_SECOND = 1000

    def hours_to_milliseconds(self, hours):
        return int(hours * self.SECONDS_PER_HOUR * self.MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.hours_to_milliseconds(2))
    print(converter.hours_to_milliseconds(5))