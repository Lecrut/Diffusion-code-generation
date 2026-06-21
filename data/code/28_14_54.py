def is_valid_number(value):
    return isinstance(value, (int, float))

def compare_floats(num1, num2):
    if not is_valid_number(num1) or not is_valid_number(num2):
        raise ValueError("Both inputs must be numbers.")
    return num1 > num2

if __name__ == '__main__':
    sample_num1 = 3.14159
    sample_num2 = 2.71828
    result_function = compare_floats(sample_num1, sample_num2)
    print("Function Result:", result_function)

    class FloatComparator:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def is_valid(self):
            return is_valid_number(self.num1) and is_valid_number(self.num2)

        def compare(self):
            if not self.is_valid():
                raise ValueError("Both inputs must be numbers.")
            return self.num1 > self.num2

    comparator = FloatComparator(3.5, 2.8)
    result_class = comparator.compare()
    print("Class Result:", result_class)