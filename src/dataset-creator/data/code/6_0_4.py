class NumericComparator:
    def is_strictly_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be numeric integers or floats.")
        try:
            return value1 > value2
        except OverflowError as e:
            raise ValueError(f"Numeric overflow occurred during comparison: {e}")
if __name__ == '__main__':
    comparator = NumericComparator()
    test_cases = [
        (5, 3),            
        (10.5, 9.2),       
        (-1, -5),          
        (42, 42),           
        ("a", 5),                            
        (float('inf'), float('-inf')),       
    ]
    for val1, val2 in test_cases:
        try:
            result = comparator.is_strictly_greater(val1, val2)
            print(f"{val1} > {val2}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error comparing {val1} and {val2}: {e}")