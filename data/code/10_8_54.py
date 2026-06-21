class TemperatureStatistics:
    DEFAULT_PRECISION = 2

    @staticmethod
    def calculate_mean(temp1, temp2):
        if not (isinstance(temp1, (int, float)) and isinstance(temp2, (int, float))):
            raise ValueError("Both temperatures must be numbers")
        return round((temp1 + temp2) / 2, TemperatureStatistics.DEFAULT_PRECISION)

if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 25.8
    mean_temperature = TemperatureStatistics.calculate_mean(sample_temp1, sample_temp2)
    print(mean_temperature)