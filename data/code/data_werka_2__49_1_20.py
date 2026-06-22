class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            return f"{self.length1} is less than {self.length2}"
        else:
            return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    comparator = LengthComparator(25, 35)
    print(comparator.compare())