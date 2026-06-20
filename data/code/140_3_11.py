class TemperatureEvaluator:
    def __init__(self):
        self.min_temp = 15
        self.max_temp = 30

    def is_safe_temperature(self, temp):
        return self.min_temp <= temp <= self.max_temp

if __name__ == '__main__':
    evaluator = TemperatureEvaluator()
    sample_temperatures = [14, 25, 31]
    results = [evaluator.is_safe_temperature(temp) for temp in sample_temperatures]
    print(results)