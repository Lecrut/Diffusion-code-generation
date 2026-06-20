class TimeConverter:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def convert_to_minutes(self) -> float:
        return (self.hours * 60) + self.minutes + (self.seconds / 60.0)

if __name__ == '__main__':
    converter = TimeConverter(1, 30, 0)
    total_minutes = converter.convert_to_minutes()
    print(f"Input Time: {converter.hours} hours, {converter.minutes} minutes, {converter.seconds} seconds")
    print(f"Total minutes: {total_minutes:.2f}")