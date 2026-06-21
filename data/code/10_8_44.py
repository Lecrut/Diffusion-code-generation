class TemperatureProcessor:

    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def validate_temperatures(self):
        if not (isinstance(self.temp1, (int, float)) and isinstance(self.temp2, (int, float))):
            raise ValueError('Both temperatures must be numbers')

    def calculate_mean(self):
        return round((self.temp1 + self.temp2) / 2, 2)
if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 25.8
    try:
        processor = TemperatureProcessor(sample_temp1, sample_temp2)
        processor.validate_temperatures()
        mean_temperature = processor.calculate_mean()
        print(mean_temperature)
    except ValueError as e:
        print(e)