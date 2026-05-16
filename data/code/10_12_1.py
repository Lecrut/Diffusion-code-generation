class TemperatureComparator:
    def compare_temperatures(self, temp1, temp2):
        if temp1 > temp2:
            return "Temperature 1 is higher"
        elif temp1 < temp2:
            return "Temperature 2 is higher"
        else:
            return "Temperatures are equal"
    def calculate_absolute_difference(self, temp1, temp2):
        return abs(temp1 - temp2)
if __name__ == '__main__':
    comparator = TemperatureComparator()
    t1 = 25.5
    t2 = 30.0
    t3 = 25.5
    print(comparator.compare_temperatures(t1, t2))
    print(comparator.compare_temperatures(t3, t1))
    print(comparator.compare_temperatures(t1, t3))
    print(f"Absolute difference between {t1} and {t2}: {comparator.calculate_absolute_difference(t1, t2)}")
    print(f"Absolute difference between {t1} and {t3}: {comparator.calculate_absolute_difference(t1, t3)}")