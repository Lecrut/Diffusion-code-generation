class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def analyze(self):
        if self.length1 > self.length2:
            print(f"{self.length1} is greater than {self.length2}")
        elif self.length1 < self.length2:
            print(f"{self.length1} is smaller than {self.length2}")
        else:
            print(f"{self.length1} is equal to {self.length2}")
if __name__ == '__main__':
    l1 = 15
    l2 = 25
    comparator1 = LengthComparator(l1, l2)
    print("--- Comparison 1 ---")
    comparator1.analyze()
    l3 = 100
    l4 = 100
    comparator2 = LengthComparator(l3, l4)
    print("\n--- Comparison 2 ---")
    comparator2.analyze()
    l5 = 5
    l6 = 3
    comparator3 = LengthComparator(l5, l6)
    print("\n--- Comparison 3 ---")
    comparator3.analyze()