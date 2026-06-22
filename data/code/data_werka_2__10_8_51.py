class TemperatureProcessor:
    def __init__(self):
        self.temperatures = {}
    
    def add_temperature(self, name, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Temperature {name} must be a number")
        self.temperatures[name] = value
    
    def calculate_mean(self):
        if len(self.temperatures) != 2:
            raise ValueError("Exactly two temperature readings are required.")
        return round(sum(self.temperatures.values()) / 2, 2)

if __name__ == '__main__':
    processor = TemperatureProcessor()
    sample_temperatures = {
        'temperature1': 30.5,
        'temperature2': 25.8
    }
    
    for name, value in sample_temperatures.items():
        processor.add_temperature(name, value)
    
    mean_temperature = processor.calculate_mean()
    print(mean_temperature)