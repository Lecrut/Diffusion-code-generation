class TimeConverter:

    def __init__(self):
        self.conversion_factor = 1 / (60 * 24)

    def convert_minutes_to_days(self, minutes):
        return minutes * self.conversion_factor
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_minutes_to_days(1440))
    print(converter.convert_minutes_to_days(720))
    print(converter.convert_minutes_to_days(360))