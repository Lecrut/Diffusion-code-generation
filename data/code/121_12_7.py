class QuantityComparator:
    def compare(self, a, b):
        if a > b:
            return f"{a} is larger than {b}"
        elif b > a:
            return f"{b} is larger than {a}"
        else:
            return f"{a} is equal to {b}"
if __name__ == '__main__':
    comparator = QuantityComparator()
    print(comparator.compare(10.5, 5.2))
    print(comparator.compare(3.14, 3.14))
    print(comparator.compare(-5.0, 0.0))
    print(comparator.compare(1.0000000000000001, 1.0))
    print(comparator.compare(100, 99.999))