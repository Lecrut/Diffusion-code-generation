class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a < length_b:
            return f"{length_a} is shorter than {length_b}"
        elif length_a > length_b:
            return f"{length_a} is longer than {length_b}"
        else:
            return f"{length_a} and {length_b} are equal"

if __name__ == '__main__':
    comparator = LengthComparator()
    
    # Sample values to test the compare method without user input
    result1 = comparator.compare(5, 10)
    print(result1)
    
    result2 = comparator.compare(7.5, 3.2)
    print(result2)
    
    result3 = comparator.compare(4, 4)
    print(result3)