class TemperatureRangeChecker:
    MIN_TEMP = -273.15

    @staticmethod
    def is_valid_temperature(temp):
        return isinstance(temp, (int, float)) and temp >= TemperatureRangeChecker.MIN_TEMP

    @staticmethod
    def is_within_range(temp, min_temp, max_temp):
        if not (TemperatureRangeChecker.is_valid_temperature(temp) and TemperatureRangeChecker.is_valid_temperature(min_temp) and TemperatureRangeChecker.is_valid_temperature(max_temp)):
            return False
        if min_temp > max_temp:
            return False
        return min_temp <= temp <= max_temp
if __name__ == '__main__':
    print(TemperatureRangeChecker.is_within_range(20, 15, 25))
    print(TemperatureRangeChecker.is_within_range(30, 20, 25))
    print(TemperatureRangeChecker.is_within_range('a', 15, 25))
    print(TemperatureRangeChecker.is_within_range(20, 25, 15))