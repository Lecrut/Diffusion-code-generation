class NumberComparator:
    def compare(self, a, b):
        if a > b:
            return f"{a} is greater than {b}"
        elif a < b:
            return f"{a} is less than {b}"
        else:
            return f"{a} equals {b}"
if __name__ == '__main__':
    comparator = NumberComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 8))
    print(comparator.compare(-5, 0))
    print(comparator.compare(100, 99))