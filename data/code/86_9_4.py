class BooleanComparator:
    def compare(self, a: bool, b: bool) -> str:
        if a == b:
            return f"{a} is equal to {b}"
        else:
            return f"{a} is not equal to {b}"

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, False)
    print(result1)
    result2 = comparator.compare(False, False)
    print(result2)