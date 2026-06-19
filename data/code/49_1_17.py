class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length2 > self.length1:
            return f"{self.length2} is greater than {self.length1}"
        else:
            return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    comparator1 = LengthComparator(50, 30)
    print(comparator1.compare())

    comparator2 = LengthComparator(20, 20)
    print(comparator2.compare())

    comparator3 = LengthComparator(75, 100)
    print(comparator3.compare())