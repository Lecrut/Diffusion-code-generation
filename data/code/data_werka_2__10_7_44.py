class TemperatureComparer:
    TOLERANCE = 1

    @staticmethod
    def within_tolerance(temp1, temp2):
        return abs(temp1 - temp2) <= TemperatureComparer.TOLERANCE

if __name__ == '__main__':
    temperature1 = 15.0
    temperature2 = 16.5
    result = TemperatureComparer.within_tolerance(temperature1, temperature2)
    print(result)