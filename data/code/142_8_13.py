class BooleanComparator:
    def __init__(self, bool1, bool2):
        self.bool1 = bool1
        self.bool2 = bool2

    def compare(self):
        return self.bool1 == self.bool2

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(comparator.compare())