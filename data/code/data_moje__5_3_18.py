class LengthComparator:
    def __init__(self, length_a, length_b):
        self.length_a = length_a
        self.length_b = length_b

    def get_difference(self):
        return abs(self.length_a - self.length_b)

    def compare(self):
        if self.length_a > self.length_b:
            return f"Length A is longer than Length B by {self.get_difference()} units"
        if self.length_b > self.length_a:
            return f"Length B is longer than Length A by {self.get_difference()} units"
        return "Length A and Length B are equal"

if __name__ == '__main__':
    a = 25
    b = 18
    comparator = LengthComparator(a, b)
    print(comparator.compare())
    print(comparator.get_difference())