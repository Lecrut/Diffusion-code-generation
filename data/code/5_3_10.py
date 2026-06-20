class LengthComparator:
    def __init__(self, length_a, length_b):
        self.validate_length(length_a)
        self.validate_length(length_b)
        self.length_a = length_a
        self.length_b = length_b

    @staticmethod
    def validate_length(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be a numeric type")
        if value < 0:
            raise ValueError("Length cannot be negative")

    def compare(self):
        diff = self.length_a - self.length_b
        if diff > 0:
            return f"Length A is longer than Length B by {diff} units"
        elif diff < 0:
            return f"Length B is longer than Length A by {abs(diff)} units"
        else:
            return "Length A and Length B are equal"

if __name__ == '__main__':
    a = 20.5
    b = 15.0
    comparator = LengthComparator(a, b)
    output = comparator.compare()
    print(output)