class TimeConverter:
    MINUTES_PER_DAY = 1440.0

    @staticmethod
    def convert_minutes_to_days(minutes):
        return minutes / TimeConverter.MINUTES_PER_DAY

if __name__ == '__main__':
    sample_minutes = 2880
    days = TimeConverter.convert_minutes_to_days(sample_minutes)
    print(days)