def compare_floats(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return num1 > num2

class FloatComparison:
    def __init__(self, value_map):
        self.value_map = value_map
    
    def get_comparison_result(self, key1, key2):
        if key1 not in self.value_map or key2 not in self.value_map:
            raise KeyError("One or both keys are missing from the value map.")
        return compare_floats(self.value_map[key1], self.value_map[key2])

if __name__ == '__main__':
    sample_values = {
        'pi': 3.14159,
        'e': 2.71828,
        'sqrt2': 1.41421
    }
    
    comparator = FloatComparison(sample_values)
    result_function = compare_floats(3.5, 2.8)
    print("Function Result:", result_function)
    
    class_result = comparator.get_comparison_result('pi', 'e')
    print("Class Result:", class_result)