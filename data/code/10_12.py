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
    comparison_result = comparator.compare_temperatures(temp_a, temp_b)
    print(f"Comparison between {temp_a}°C and {temp_b}°C: {comparison_result}")
    difference = comparator.calculate_absolute_difference(temp_a, temp_b)
    print(f"Absolute difference between {temp_a}°C and {temp_b}°C: {difference}°C")
    temp_c = 15.0
    temp_d = 15.0
    comparison_result_equal = comparator.compare_temperatures(temp_c, temp_d)
    print(f"Comparison between {temp_c}°C and {temp_d}°C: {comparison_result_equal}")
    difference_equal = comparator.calculate_absolute_difference(temp_c, temp_d)
    print(f"Absolute difference between {temp_c}°C and {temp_d}°C: {difference_equal}°C")