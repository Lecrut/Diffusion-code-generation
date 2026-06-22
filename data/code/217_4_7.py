class NumberComparator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def compare(self):
        return f'a {">=" if self.num1 >= self.num2 else "<"} b' if self.num1 != self.num2 else 'a == b'

if __name__ == '__main__':
    comparator1 = NumberComparator(42, 17)
    print(comparator1.compare())

    comparator2 = NumberComparator(5, 3)
    print(comparator2.compare())

    comparator3 = NumberComparator(2, 4)
    print(comparator3.compare())

    comparator4 = NumberComparator(7, 7)
    print(comparator4.compare())