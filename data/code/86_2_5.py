class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample_a = False
    sample_b = True
    result = comparator.check_equality(sample_a, sample_b)
    print(f"Equality of {sample_a} and {sample_b}: {result}")