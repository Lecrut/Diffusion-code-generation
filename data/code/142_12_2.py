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
    b1 = True
    b2 = True
    result1, message1 = BooleanComparator.compare_booleans(b1, b2)
    print(f"Comparing {b1} and {b2}: Result={result1}, Message='{message1}'")
    b3 = False
    b4 = True
    result2, message2 = BooleanComparator.compare_booleans(b3, b4)
    print(f"Comparing {b3} and {b4}: Result={result2}, Message='{message2}'")
    b5 = False
    b6 = False
    result3, message3 = BooleanComparator.compare_booleans(b5, b6)
    print(f"Comparing {b5} and {b6}: Result={result3}, Message='{message3}'")