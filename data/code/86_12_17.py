class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

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