import math

class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        epsilon = 1e-9
        if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
            raise ValueError("Both lengths must be numbers.")
        
        diff = abs(self.length1 - self.length2)
        if diff < epsilon:
            return "equal"
        elif self.length1 > self.length2:
            return "greater"
        else:
            return "smaller"

if __name__ == '__main__':
    try:
        comparator1 = LengthComparator(10.0, 5.0)
        result1 = comparator1.compare()
        print(f"Comparison 1: {result1}")

        comparator2 = LengthComparator(20.0, 20.0)
        result2 = comparator2.compare()
        print(f"\nComparison 2: {result2}")

        comparator3 = LengthComparator(3.0, 15.0)
        result3 = comparator3.compare()
        print(f"\nComparison 3: {result3}")
    except ValueError as e:
        print(e)