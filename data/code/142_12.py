class BooleanComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
        result = a == b
        if result:
            outcome = "Equal"
        else:
            outcome = "Not Equal"
        return result, outcome
if __name__ == '__main__':
    val1 = True
    val2 = True
    result1, outcome1 = BooleanComparator.compare_booleans(val1, val2)
    print(f"Comparing {val1} and {val2}: Result={result1}, Outcome='{outcome1}'")
    val3 = False
    val4 = True
    result2, outcome2 = BooleanComparator.compare_booleans(val3, val4)
    print(f"Comparing {val3} and {val4}: Result={result2}, Outcome='{outcome2}'")
    val5 = False
    val6 = False
    result3, outcome3 = BooleanComparator.compare_booleans(val5, val6)
    print(f"Comparing {val5} and {val6}: Result={result3}, Outcome='{outcome3}'")