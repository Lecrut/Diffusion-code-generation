class TemperatureProcessor:
    def __init__(self, temp1, temp2):
        self.validate_temperatures(temp1, temp2)
        self.temp1 = temp1
        self.temp2 = temp2

    def validate_temperatures(self, temp1, temp2):
        if not (isinstance(temp1, (int, float)) and isinstance(temp2, (int, float))):
            raise ValueError("Both temperatures must be numbers")

    def calculate_mean(self):
        return round((self.temp1 + self.temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 35.7
    sample_temp2 = 40.2
    processor = TemperatureProcessor(sample_temp1, sample_temp2)
    mean_temperature = processor.calculate_mean()
    print(mean_temperature)