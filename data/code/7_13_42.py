class TimeConverter:
    def __init__(self):
        self.time_units = {
            'hour': 3600,
            'minute': 60,
            'second': 1
        }

    def convert_to_seconds(self, hours, minutes, seconds):
        total_seconds = (hours * self.time_units['hour'] +
                         minutes * self.time_units['minute'] +
                         seconds * self.time_units['second'])
        return total_seconds

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 3
    sample_minutes = 15
    sample_seconds = 45
    total_seconds = converter.convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)