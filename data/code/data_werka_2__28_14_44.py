def compare_floats(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return num1 > num2

class FloatComparator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def compare(self):
        if not isinstance(self.num1, (int, float)) or not isinstance(self.num2, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return self.num1 > self.num2

if __name__ == '__main__':
    sample_num1 = 5.0
    sample_num2 = 3.0
    result_function = compare_floats(sample_num1, sample_num2)
    print("Function Result:", result_function)
    
    comparator = FloatComparator(4.5, 6.7)
    result_class = comparator.compare()
    print("Class Result:", result_class)