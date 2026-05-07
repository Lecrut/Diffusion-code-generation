class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b
if __name__ == '__main__':
    comparator = BooleanComparator()
    print(f"Equality of True and True: {comparator.check_equality(True, True)}")
    print(f"Equality of True and False: {comparator.check_equality(True, False)}")
    print(f"Equality of False and False: {comparator.check_equality(False, False)}")
    print(f"Equality of False and True: {comparator.check_equality(False, True)}")