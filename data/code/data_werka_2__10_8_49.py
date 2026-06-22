class TemperatureStatistics:
    def __init__(self, temp1, temp2):
        self.temperatures = [temp1, temp2]
    
    def validate_temperatures(self):
        if len(self.temperatures) != 2 or not all(isinstance(temp, (int, float)) for temp in self.temperatures):
            raise ValueError("Exactly two numeric temperature readings are required.")
    
    def calculate_mean(self):
        return round(sum(self.temperatures) / len(self.temperatures), 2)
    
    def display_temperatures(self):
        return f"Temperature 1: {self.temperatures[0]}, Temperature 2: {self.temperatures[1]}"

if __name__ == '__main__':
    sample_temp1 = 35.7
    sample_temp2 = 40.2
    stats = TemperatureStatistics(sample_temp1, sample_temp2)
    
    try:
        stats.validate_temperatures()
        mean_temperature = stats.calculate_mean()
        print(f"Mean Temperature: {mean_temperature}")
        print(stats.display_temperatures())
    except ValueError as e:
        print(e)