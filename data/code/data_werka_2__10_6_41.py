class TemperatureComparator:
    def compare(self, temp1, temp2):
        if temp1 > temp2:
            return "Temp1 is higher than Temp2"
        elif temp1 < temp2:
            return "Temp1 is lower than Temp2"
        else:
            return "Temperatures are equal"

def test_temperature_comparator():
    comparator = TemperatureComparator()
    assert comparator.compare(30, 25) == "Temp1 is higher than Temp2"
    assert comparator.compare(20, 25) == "Temp1 is lower than Temp2"
    assert comparator.compare(25, 25) == "Temperatures are equal"

if __name__ == '__main__':
    test_temperature_comparator()
    comparator = TemperatureComparator()
    print(comparator.compare(30, 25))
    print(comparator.compare(20, 25))
    print(comparator.compare(25, 25))