class TemperatureComparator:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        if self.temp1 > self.temp2:
            return "First temperature is higher"
        elif self.temp1 < self.temp2:
            return "Second temperature is higher"
        else:
            return "Temperatures are equal"

def test_temperature_comparator():
    comparator = TemperatureComparator(30, 25)
    assert comparator.compare() == "First temperature is higher"
    
    comparator = TemperatureComparator(20, 25)
    assert comparator.compare() == "Second temperature is higher"
    
    comparator = TemperatureComparator(25, 25)
    assert comparator.compare() == "Temperatures are equal"

if __name__ == '__main__':
    test_temperature_comparator()
    
    temp1 = 30
    temp2 = 25
    comparator = TemperatureComparator(temp1, temp2)
    print(comparator.compare())
    
    temp1 = 20
    temp2 = 40
    comparator = TemperatureComparator(temp1, temp2)
    print(comparator.compare())
    
    temp1 = 25
    temp2 = 25
    comparator = TemperatureComparator(temp1, temp2)
    print(comparator.compare())