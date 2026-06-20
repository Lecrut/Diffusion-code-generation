class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample1 = True
    sample2 = False
    print(f"Equality of {sample1} and {sample2}: {comparator.check_equality(sample1, sample2)}")