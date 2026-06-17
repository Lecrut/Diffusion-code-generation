class NumberComparator:
    def compare(self, a, b):
        if a > b:
            return f"{a} is larger than {b}"
        elif b > a:
            return f"{b} is larger than {a}"
        else:
            return f"{a} and {b} are equal"
if __name__ == '__main__':
    comparator = NumberComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(3, 12))
    print(comparator.compare(7, 7))
    print(comparator.compare(-2, 4))