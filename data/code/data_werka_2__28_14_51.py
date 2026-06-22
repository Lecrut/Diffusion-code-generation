def compare_floats(num1, num2):
    return num1 > num2

class NumberComparison:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def is_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    sample_values = {
        'num1': 3.14159,
        'num2': 2.71828
    }
    
    result_function = compare_floats(sample_values['num1'], sample_values['num2'])
    print("Function Result:", result_function)
    
    comparator = NumberComparison(3.5, 2.8)
    result_class = comparator.is_greater()
    print("Class Result:", result_class)