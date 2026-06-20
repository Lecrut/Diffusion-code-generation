class BooleanComparator:
    def compare(self, a: bool, b: bool) -> str:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values.")
        return f"{a} is equal to {b}" if a == b else f"{a} is not equal to {b}"

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, False)
    result2 = comparator.compare(False, False)
    print(result1)
    print(result2)