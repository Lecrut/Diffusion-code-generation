class TimeConverter:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def to_hours(self):
        return self.total_seconds // 3600

    def to_minutes(self):
        return self.total_seconds % 3600 // 60

    def to_seconds(self):
        return self.total_seconds % 60

    def convert_to(self, target_unit):
        if target_unit == 'hours':
            return self.to_hours()
        elif target_unit == 'minutes':
            return self.to_minutes()
        elif target_unit == 'seconds':
            return self.to_seconds()
        else:
            raise ValueError("Unsupported unit. Use 'hours', 'minutes', or 'seconds'.")
if __name__ == '__main__':
    converter = TimeConverter(2, 30, 45)
    print(converter.convert_to('hours'))
    print(converter.convert_to('minutes'))
    print(converter.convert_to('seconds'))