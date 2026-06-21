class TemperatureComparator:
    GREATER = "First temperature is greater than the second"
    LESS = "First temperature is less than the second"
    EQUAL = "Both temperatures are equal"

    @staticmethod
    def compare_temperatures(temp1, temp2):
        if temp1 > temp2:
            return TemperatureComparator.GREATER
        elif temp1 < temp2:
            return TemperatureComparator.LESS
        else:
            return TemperatureComparator.EQUAL

def test_temperature_comparator():
    assert TemperatureComparator.compare_temperatures(30, 25) == TemperatureComparator.GREATER
    assert TemperatureComparator.compare_temperatures(20, 25) == TemperatureComparator.LESS
    assert TemperatureComparator.compare_temperatures(25, 25) == TemperatureComparator.EQUAL

if __name__ == '__main__':
    test_temperature_comparator()
    print(TemperatureComparator.compare_temperatures(30, 25))
    print(TemperatureComparator.compare_temperatures(20, 25))
    print(TemperatureComparator.compare_temperatures(25, 25))