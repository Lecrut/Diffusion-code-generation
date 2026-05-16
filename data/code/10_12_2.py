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
    temp_a = 25.5
    temp_b = 30.0
    temp_c = 25.5
    print(comparator.compare_temperatures(temp_a, temp_b))
    print(comparator.compare_temperatures(temp_c, temp_a))
    print(comparator.calculate_absolute_difference(temp_a, temp_b))
    print(comparator.calculate_absolute_difference(temp_a, temp_c))