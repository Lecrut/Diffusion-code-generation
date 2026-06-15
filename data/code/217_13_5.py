class NumberComparator:
    def compare(self, a, b):
        if a > b:
            return f"{a} is greater than {b}"
        elif a == b:
            return f"{a} equals {b}"
        else:
            return f"{a} is less than {b}"
if __name__ == '__main__':
    comparator = NumberComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(7, 7))
    print(comparator.compare(3, 12))
    print(comparator.compare(-5, 0))