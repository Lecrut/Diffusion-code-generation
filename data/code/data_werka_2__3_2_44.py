class TemperatureFilter:
    FREEZING_POINT = 0

    def __init__(self, temperatures):
        self.temperatures = temperatures

    def filter_above_freezing(self):
        return [temp for temp in self.temperatures if temp >= self.FREEZING_POINT]

if __name__ == '__main__':
    sample_temperatures = [-10, 0, 5, -3, 8, -7, 4]
    temperature_filter = TemperatureFilter(sample_temperatures)
    filtered_temperatures = temperature_filter.filter_above_freezing()
    print(filtered_temperatures)