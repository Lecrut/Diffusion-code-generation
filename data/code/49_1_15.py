class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return f"Length 1: {self.length1} is greater than Length 2: {self.length2}"
        elif self.length2 > self.length1:
            return f"Length 1: {self.length1} is less than Length 2: {self.length2}"
        else:
            return f"Length 1: {self.length1} is equal to Length 2: {self.length2}"

if __name__ == '__main__':
    comparator1 = LengthComparator(10, 25)
    print(comparator1.compare())
    
    comparator2 = LengthComparator(50, 50)
    print(comparator2.compare())
    
    comparator3 = LengthComparator(100, 10)
    print(comparator3.compare())