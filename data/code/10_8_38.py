class TemperatureCalculator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def calculate_mean(self):
        return round((self.temp1 + self.temp2) / 2, 2)

if __name__ == '__main__':
    sample_temperatures = {
        'temp1': 30.5,
        'temp2': 25.8
    }
    calculator = TemperatureCalculator(sample_temperatures['temp1'], sample_temperatures['temp2'])
    mean_temperature = calculator.calculate_mean()
    print(mean_temperature)