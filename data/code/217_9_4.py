class NumberComparator:
    def compare_strictly_greater(self, num1, num2):
        return num1 > num2
if __name__ == '__main__':
    comparator = NumberComparator()
    a = 10
    b = 5
    c = 10
    d = 10.0
    print(f"Is {a} strictly greater than {b}? {comparator.compare_strictly_greater(a, b)}")
    print(f"Is {c} strictly greater than {d}? {comparator.compare_strictly_greater(c, d)}")
    print(f"Is {b} strictly greater than {a}? {comparator.compare_strictly_greater(b, a)}")