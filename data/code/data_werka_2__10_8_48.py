class TemperatureProcessor:
    def __init__(self, temperatures):
        if len(temperatures) != 2:
            raise ValueError("Exactly two temperature readings are required.")
        self.temperatures = temperatures
    
    def validate_temperatures(self):
        for temp in self.temperatures:
            if not isinstance(temp, (int, float)):
                raise ValueError(f"Invalid temperature value: {temp}. Must be a number.")
    
    def calculate_mean(self):
        self.validate_temperatures()
        return round(sum(self.temperatures) / len(self.temperatures), 2)

if __name__ == '__main__':
    sample_temps = [30.5, 25.8]
    processor = TemperatureProcessor(sample_temps)
    mean_temperature = processor.calculate_mean()
    print(mean_temperature)