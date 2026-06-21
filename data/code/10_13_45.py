class TemperatureComparison:
    @staticmethod
    def is_first_temp_greater(temp1, temp2):
        if not isinstance(temp1, int) or not isinstance(temp2, int):
            raise ValueError("Both temperatures must be integers.")
        return temp1 > temp2

if __name__ == '__main__':
    sample_value_one = 50
    sample_value_two = 45
    comparison_result = TemperatureComparison.is_first_temp_greater(sample_value_one, sample_value_two)
    print(comparison_result)