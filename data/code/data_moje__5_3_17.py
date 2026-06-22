class LengthComparator:
    def __init__(self, length_a, length_b):
        if not isinstance(length_a, (int, float)) or not isinstance(length_b, (int, float)):
            raise TypeError("Both inputs must be numeric values")
        self.length_a = length_a
        self.length_b = length_b

    def compare(self):
        if self.length_a > self.length_b:
            difference = self.length_a - self.length_b
            return f"Length A is longer than Length B by {difference} units"
        elif self.length_b > self.length_a:
            difference = self.length_b - self.length_a
            return f"Length B is longer than Length A by {difference} units"
        else:
            return "Length A and Length B are equal"

if __name__ == '__main__':
    comparator = LengthComparator(25.5, 12.0)
    print(comparator.compare())