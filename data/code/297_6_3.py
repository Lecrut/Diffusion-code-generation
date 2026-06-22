class TimeConverter:
    def __init__(self):
        self.seconds_per_hour = 3600
        self.milliseconds_per_second = 1000

    def hours_to_milliseconds(self, hours):
        return int(hours * self.seconds_per_hour * self.milliseconds_per_second)

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {converter.hours_to_milliseconds(sample_hours_1)} milliseconds")
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {converter.hours_to_milliseconds(sample_hours_2)} milliseconds")