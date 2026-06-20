class LengthComparator:
    def __init__(self, length_a, length_b):
        self.length_a = length_a
        self.length_b = length_b

    def compare(self):
        if self.length_a < 0 or self.length_b < 0:
            raise ValueError("Length cannot be negative")
        if self.length_a == self.length_b:
            return "equal"
        elif self.length_a > self.length_b:
            return f"a is greater than b by {self.length_a - self.length_b}"
        else:
            return f"b is greater than a by {self.length_b - self.length_a}"

if __name__ == '__main__':
    comp = LengthComparator(10, 15)
    print(comp.compare())
    try:
        bad_comp = LengthComparator(-5, 10)
        bad_comp.compare()
    except ValueError as e:
        print(str(e))