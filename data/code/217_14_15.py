class NumberComparator:
    def compare(self, a, b):
        if a < b:
            return f"{a} is less than {b}"
        elif a > b:
            return f"{a} is greater than {b}"
        else:
            return f"{a} is equal to {b}"

if __name__ == '__main__':
    comparator = NumberComparator()
    result1 = comparator.compare(5, 10)
    print(result1)
    result2 = comparator.compare(-3, 7)
    print(result2)
    result3 = comparator.compare(42, 42)
    print(result3)