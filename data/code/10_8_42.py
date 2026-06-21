class TemperatureProcessor:
    def __init__(self, readings):
        if len(readings) != 2 or not all(isinstance(temp, (int, float)) for temp in readings):
            raise ValueError("Exactly two numeric temperature readings are required.")
        self.readings = readings

    def compute_mean(self):
        return round(sum(self.readings) / len(self.readings), 2)

if __name__ == '__main__':
    sample_readings = {
        'reading1': 30.5,
        'reading2': 25.8
    }
    processor = TemperatureProcessor([sample_readings['reading1'], sample_readings['reading2']])
    mean_temperature = processor.compute_mean()
    print(mean_temperature)