class TimeConverter:
    def __init__(self):
        self.time_units = {
            'hours': 3600,
            'minutes': 60,
            'seconds': 1
        }
    
    def convert_to_seconds(self, hours, minutes, seconds):
        total_seconds = (hours * self.time_units['hours'] +
                         minutes * self.time_units['minutes'] +
                         seconds * self.time_units['seconds'])
        return total_seconds

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 4
    sample_minutes = 30
    sample_seconds = 10
    total_seconds = converter.convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)