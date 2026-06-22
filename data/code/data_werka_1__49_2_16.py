class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def compare(self):
        if self.length1 > self.length2:
            return "Length 1 is greater than Length 2"
        elif self.length1 < self.length2:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"

if __name__ == '__main__':
    length_1_value = '5.7'
    length_2_value = '3.9'
    
    comparator = LengthComparator(length_1_value, length_2_value)
    comparison_result = comparator.compare()
    
    print(f"Length 1: {length_1_value}")
    print(f"Length 2: {length_2_value}")
    print(f"Comparison Result: {comparison_result}")