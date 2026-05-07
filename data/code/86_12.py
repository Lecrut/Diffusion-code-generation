class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> str:
        if a == b:
            return 'Equal'
        else:
            return 'Not Equal'
if __name__ == '__main__':
    comparator = BooleanComparator()
    val1_a = True
    val1_b = True
    result1 = comparator.check_equality(val1_a, val1_b)
    print(f"Comparing {val1_a} and {val1_b}: {result1}")
    val2_a = True
    val2_b = False
    result2 = comparator.check_equality(val2_a, val2_b)
    print(f"Comparing {val2_a} and {val2_b}: {result2}")
    val3_a = False
    val3_b = True
    result3 = comparator.check_equality(val3_a, val3_b)
    print(f"Comparing {val3_a} and {val3_b}: {result3}")
    val4_a = False
    val4_b = False
    result4 = comparator.check_equality(val4_a, val4_b)
    print(f"Comparing {val4_a} and {val4_b}: {result4}")