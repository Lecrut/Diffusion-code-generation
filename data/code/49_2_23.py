class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def compare(self):
        if self.length1 > self.length2:
            return f"{self.length1} is longer than {self.length2}."
        elif self.length1 < self.length2:
            return f"{self.length2} is longer than {self.length1}."
        else:
            return "Both lengths are equal."

if __name__ == '__main__':
    comparator = LengthComparator(7.8, 4.6)
    print(comparator.compare())