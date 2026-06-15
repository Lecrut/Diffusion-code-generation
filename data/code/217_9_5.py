class NumberComparator:
    def compare_greater_than(self, num1, num2):
        return num1 > num2
if __name__ == '__main__':
    comparator = NumberComparator()
    a = 10
    b = 5
    c = 10
    d = 20
    print(f"Is {a} strictly greater than {b}? {comparator.compare_greater_than(a, b)}")
    print(f"Is {c} strictly greater than {d}? {comparator.compare_greater_than(c, d)}")