def compare_floats(num1, num2):
    return num1 > num2

class FloatComparison:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
    
    def is_first_greater(self):
        return self.first_number > self.second_number

if __name__ == '__main__':
    sample_value1 = 4.56789
    sample_value2 = 3.14159
    direct_comparison_result = compare_floats(sample_value1, sample_value2)
    print("Direct Comparison Result:", direct_comparison_result)

    comparison_instance = FloatComparison(5.0, 4.9)
    instance_comparison_result = comparison_instance.is_first_greater()
    print("Instance Comparison Result:", instance_comparison_result)