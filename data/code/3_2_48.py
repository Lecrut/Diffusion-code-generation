class TemperatureFilter:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def filter_above_freezing(self):
        freezing_point = 0
        filtered_temps = []
        for temp in self.temperatures:
            if temp >= freezing_point:
                filtered_temps.append(temp)
        return filtered_temps

if __name__ == '__main__':
    sample_temperatures = [-1, -3, 2, 7, -5, 0, 9]
    temp_filter = TemperatureFilter(sample_temperatures)
    filtered_temperatures = temp_filter.filter_above_freezing()
    print(filtered_temperatures)