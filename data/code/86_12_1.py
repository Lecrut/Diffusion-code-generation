class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> str:
        if a == b:
            return 'Equal'
        else:
            return 'Not Equal'
if __name__ == '__main__':
    comparator = BooleanComparator()
    val1 = True
    val2 = True
    result1 = comparator.check_equality(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = False
    val4 = True
    result2 = comparator.check_equality(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = False
    val6 = False
    result3 = comparator.check_equality(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")