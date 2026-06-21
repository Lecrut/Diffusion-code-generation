class TemperatureComparator:
    @staticmethod
    def compare_temperatures(temp1, temp2):
        return max(temp1, temp2)

if __name__ == '__main__':
    sample_temp1 = 29.0
    sample_temp2 = 31.4
    higher_temperature = TemperatureComparator.compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)