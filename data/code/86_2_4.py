class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample_true = True
    sample_false = False
    print(f"Equality of {sample_true} and {sample_true}: {comparator.check_equality(sample_true, sample_true)}")
    print(f"Equality of {sample_true} and {sample_false}: {comparator.check_equality(sample_true, sample_false)}")
    print(f"Equality of {sample_false} and {sample_true}: {comparator.check_equality(sample_false, sample_true)}")
    print(f"Equality of {sample_false} and {sample_false}: {comparator.check_equality(sample_false, sample_false)}")