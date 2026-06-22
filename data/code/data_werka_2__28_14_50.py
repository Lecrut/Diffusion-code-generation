def validate_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers.")

def compare_floats(num1, num2):
    validate_numbers(num1, num2)
    return num1 > num2

class FloatComparison:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def perform_comparison(self):
        validate_numbers(self.num1, self.num2)
        return self.num1 > self.num2

if __name__ == '__main__':
    sample_num1 = 3.14159
    sample_num2 = 2.71828
    result_function = compare_floats(sample_num1, sample_num2)
    print("Function Result:", result_function)
    
    comparator = FloatComparison(3.5, 2.8)
    result_class = comparator.perform_comparison()
    print("Class Result:", result_class)