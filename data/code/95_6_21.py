class TripleConditionProcessor:
    def __init__(self, a, b, c):
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            raise ValueError("Inputs must be integers.")
        if a == 0:
            raise ValueError("Attribute 'a' cannot be zero for division.")
        self.a = a
        self.b = b
        self.c = c

    def get_combined_result(self):
        if self.a <= 0:
            return False
        if self.b % 2 != 0:
            return False
        if self.c % self.a != 0:
            return False
        return True

    def analyze(self):
        status_a = "positive" if self.a > 0 else "non-positive"
        status_b = "even" if self.b % 2 == 0 else "odd"
        status_c = "divisible" if self.c % self.a == 0 else "not divisible"
        return (status_a, status_b, status_c)

if __name__ == '__main__':
    processor = TripleConditionProcessor(2, 4, 8)
    print(processor.get_combined_result())
    print(processor.analyze())