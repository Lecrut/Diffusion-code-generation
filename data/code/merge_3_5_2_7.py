class LengthComparator:
    def compare(self, length_a, length_b):
        if isinstance(length_a, (int, float)) and isinstance(length_b, (int, float)):
            difference = length_a - length_b
            
            if difference > 0:
                return f"{length_a} is greater than {length_b}"
            elif difference < 0:
                return f"{length_a} is less than {length_b}"
            else:
                return f"{length_a} is equal to {length_b}"
        else:
            raise TypeError("Both length arguments must be numeric.")

if __name__ == '__main__':
    comparator = LengthComparator()
    
    test_cases = [
        (10, 5),
        (3.5, 7.2),
        (4, 4),
        (-2, -8)
    ]
    
    for a_val, b_val in test_cases:
        result = comparator.compare(a_val, b_val)
        print(f"Comparing {a_val} and {b_val}: '{result}'")