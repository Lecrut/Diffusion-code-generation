class TimeConverter:
    MINUTES_PER_DAY = 1440.0

    def minutes_to_days(self, minutes):
        return minutes / self.MINUTES_PER_DAY
if __name__ == '__main__':
    converter = TimeConverter()
    sample_minutes = 2880
    result = converter.minutes_to_days(sample_minutes)
    print(result)