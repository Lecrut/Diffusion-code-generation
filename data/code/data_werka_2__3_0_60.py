class TemperatureCalculator:
    MIN_TEMPERATURE = -100.0

    @staticmethod
    def calculate_average_temperature(temperatures):
        if not temperatures:
            raise ValueError('The list of temperatures cannot be empty.')
        if any((temp < TemperatureCalculator.MIN_TEMPERATURE for temp in temperatures)):
            raise ValueError('Temperature readings must be above the minimum threshold.')
        return sum(temperatures) / len(temperatures)
if __name__ == '__main__':
    sample_temperatures = [20.5, 21.3, 19.8, 22.6, 23.4]
    average_temperature = TemperatureCalculator.calculate_average_temperature(sample_temperatures)
    print(average_temperature)