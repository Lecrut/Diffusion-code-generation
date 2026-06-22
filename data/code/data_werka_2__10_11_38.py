class TemperatureCalculator:
    @staticmethod
    def calculate_difference(temp1, temp2):
        return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temp1 = 37.5
    sample_temp2 = 40.2
    result = TemperatureCalculator.calculate_difference(sample_temp1, sample_temp2)
    print(result)