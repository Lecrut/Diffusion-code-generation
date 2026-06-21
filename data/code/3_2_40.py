class TemperatureFilter:
    FREEZING_POINT = 0

    @staticmethod
    def filter_above_freezing(temperatures):
        return [temp for temp in temperatures if temp >= TemperatureFilter.FREEZING_POINT]

if __name__ == '__main__':
    sample_temperatures = [-1, 2, -3, 4, 0, -5, 6]
    filtered_temperatures = TemperatureFilter.filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)