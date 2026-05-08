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
    print(comparator.compare(3.14159, 3.14158))
    print(comparator.compare(7, 7))
    print(comparator.compare(-1.5, 0.5))