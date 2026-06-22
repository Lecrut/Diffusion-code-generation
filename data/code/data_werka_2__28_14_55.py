def compare_floats(num1, num2):
    return num1 > num2

class ComparisonResult:
    def __init__(self, result):
        self.result = result

    def is_greater(self):
        return self.result

if __name__ == '__main__':
    sample_values = {
        'num1': 3.14159,
        'num2': 2.71828
    }
    
    result_function = compare_floats(sample_values['num1'], sample_values['num2'])
    print("Function Result:", result_function)
    
    comparator = ComparisonResult(compare_floats(3.5, 2.8))
    print("Class Method Result:", comparator.is_greater())