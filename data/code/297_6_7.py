class TimeConverter:
    def __init__(self):
        self.seconds_per_hour = 3600
        self.milliseconds_per_second = 1000
    
    def hours_to_milliseconds(self, hours):
        return int(hours * self.seconds_per_hour * self.milliseconds_per_second)

if __name__ == '__main__':
    converter = TimeConverter()
    print(f"2 hours is {converter.hours_to_milliseconds(2)} milliseconds")
    print(f"5 hours is {converter.hours_to_milliseconds(5)} milliseconds")