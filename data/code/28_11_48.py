class NumberComparator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def is_larger(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    comparator1 = NumberComparator(10, 5)
    print(comparator1.is_larger())

    comparator2 = NumberComparator(3, 7)
    print(comparator2.is_larger())

    comparator3 = NumberComparator(-1, -5)
    print(comparator3.is_larger())

    comparator4 = NumberComparator(0, 0)
    print(comparator4.is_larger())