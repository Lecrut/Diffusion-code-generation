class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def compare(self):
        if self.length1 > self.length2:
            return "Length 1 is greater than Length 2"
        elif self.length1 < self.length2:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"

if __name__ == '__main__':
    length1 = '5.5'
    length2 = '3.2'
    comparator = LengthComparator(length1, length2)
    print(comparator.compare())