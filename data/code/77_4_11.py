class TimeConverter:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_minutes(self):
        return (self.hours * 60) + self.minutes + (self.seconds / 60.0)

if __name__ == '__main__':
    converter = TimeConverter(1, 30, 0)
    print(f"Total minutes: {converter.to_minutes():.2f}")