class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    for val1, val2 in sample_values:
        print(f"Equality of {val1} and {val2}: {comparator.check_equality(val1, val2)}")