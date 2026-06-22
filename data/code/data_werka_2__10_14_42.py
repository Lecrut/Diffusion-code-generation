class TemperatureComparator:
    DEFAULT_TEMP1 = 24.6
    DEFAULT_TEMP2 = 28.9

    @staticmethod
    def compare_temperatures(temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError("Both temperatures must be integers or floats.")
        return max(temp1, temp2)

if __name__ == '__main__':
    sample_temp1 = TemperatureComparator.DEFAULT_TEMP1
    sample_temp2 = TemperatureComparator.DEFAULT_TEMP2
    higher_temperature = TemperatureComparator.compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)