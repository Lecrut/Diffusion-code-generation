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
    bool1 = True
    bool2 = True
    result1, outcome1 = BooleanComparator.compare_booleans(bool1, bool2)
    print(f"Comparing {bool1} and {bool2}: Result={result1}, Outcome='{outcome1}'")
    bool3 = False
    bool4 = True
    result2, outcome2 = BooleanComparator.compare_booleans(bool3, bool4)
    print(f"Comparing {bool3} and {bool4}: Result={result2}, Outcome='{outcome2}'")
    bool5 = False
    bool6 = False
    result3, outcome3 = BooleanComparator.compare_booleans(bool5, bool6)
    print(f"Comparing {bool5} and {bool6}: Result={result3}, Outcome='{outcome3}'")