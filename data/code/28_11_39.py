class NumberComparer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def is_larger(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    comparer1 = NumberComparer(10, 5)
    print(comparer1.is_larger())

    comparer2 = NumberComparer(3, 7)
    print(comparer2.is_larger())

    comparer3 = NumberComparer(-1, -5)
    print(comparer3.is_larger())

    comparer4 = NumberComparer(0, 0)
    print(comparer4.is_larger())

    comparer5 = NumberComparer(5.5, 2)
    print(comparer5.is_larger())